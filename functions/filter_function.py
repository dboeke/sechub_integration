import os
import json
import boto3
import requests
from botocore.exceptions import ClientError

def get_param(ssm_client, param_name, encrypted):
  print("in get_param function")
  response = ssm_client.get_parameter(
    Name=param_name,
    WithDecryption=encrypted
  )
  print("after response")
  return response['Parameter']['Value']

class GraphQlException(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)

class GraphQl:
  def __init__(self, workspace: dict) -> None:
    if not workspace or type(workspace) is not dict:
      raise ValueError("workspace is missing or not dict type")

    self.__endpoint = workspace['endpoint']
    self.__access_key = workspace['access_key']
    self.__secret_access_key = workspace['secret_key']

  def get_endpoint(self) -> str:
    return self.__endpoint

  def get_access_key(self) -> str:
    return self.__access_key

  def get_secret_access_key(self) -> str:
    return self.__secret_access_key

  def run_query(self, query: str, variables: dict) -> dict:
    if not query or type(query) is not str:
      raise ValueError("query is missing or not string type")

    if not variables or type(variables) is not dict:
      raise ValueError("variables is missing or not dict type")

    # print(f"Query: {query}")
    # print(f"Variables: {variables}")
    response = requests.post(
      self.get_endpoint(),
      auth=(self.get_access_key(), self.get_secret_access_key()),
      json={'query': query, 'variables': variables}
    )

    if response.status_code != 200 or response.json().get("errors"):
      print("GraphQL query failed, throwing exception")
      raise GraphQlException(f"Query failed: {response.text}")

    response = response.json()
    print(f"Query result: {response}")

    return response

def get_control(gql, control_id):
  print("Function: get_control_state")
  query = '''
    query Control($id: ID) {
      control(id: $id) {
        state
        resource {
          akas
        }
      }
    }
  '''
  vars = {"id": control_id}  
  response = gql.run_query(query, vars)

  if "data" in response:
    print(f"Success: Control Found")
    status = response["data"]["control"]["state"]
    akas = response["data"]["control"]["resource"]["akas"]
    print(f"Control State = {status}")
    return {
      "state": status,
      "akas": akas
    }
  else:
    print("ERROR: Control Not Found")
    print(f"ControlId: {control_id}")
    print(response["errors"])
    return False

def convert_to_asff(timestamp, control, aws_metadata, resource_akas):
  finding = {
    "SchemaVersion": "2018-10-08",
    "Severity": {
      "Label": "HIGH",
      "Product": 80
    },
    "Compliance": {
      "Status": "WARNING"
    },
    "Types": ["Software and Configuration Checks/Governance/Out of Compliance"]
  }
  control_id = control["turbot"]["id"]
  region = aws_metadata["regionName"] if "regionName" in aws_metadata else "global"
  account_id = aws_metadata["accountId"]
  finding["Id"] = f"arn:aws:securityhub:{region}:{account_id}:turbot/{control_id}"
  finding["CreatedAt"] = timestamp
  finding["UpdatedAt"] = timestamp
  AWS_REGION = os.environ['AWS_REGION']
  finding["ProductArn"] = f"arn:aws:securityhub:{AWS_REGION}:453761072151:product/turbot/turbot"
  finding["AwsAccountId"] = account_id
  control_reason = control["reason"]
  finding["Description"] = control_reason if control_reason else "No reason given"
  control_type = control["type"]["trunk"]["title"]
  finding["Title"] = f"Alarm: {control_type}"
  resources = []
  for aka in resource_akas:
    resource_aka = {
      "Type": "Resource AKA",
      "Id": aka,
      "Tags": {
        "Source": "Turbot-Sec-Hub-Integration"
      }
    }
    if "partition" in aws_metadata:
      resource_aka["Partition"] = aws_metadata["partition"]
    if "regionName" in aws_metadata:
      resource_aka["Region"] = aws_metadata["regionName"]
    resources.append(resource_aka)
  resource_id = {
    "Type": "Resource ID",
    "Id": finding["Id"]
  }
  resources.append(resource_id)
  finding["Resources"] = resources
  generator_id = control_type.replace(" > ", "-").replace(" ", "-").lower()
  finding["GeneratorId"] = f"arn:aws:securityhub:::ruleset/turbot/{generator_id}"
  print("[INFO] Create finding complete")
  print(finding)
  return finding

def lambda_handler(event, context):
  print("Parse Lambda Params")
  AWS_REGION = os.environ['AWS_REGION']
  WORKSPACE_NAME = os.environ['WORKSPACE_NAME']
  FINDINGS_QUEUE_URL = os.environ['FINDINGS_QUEUE_URL']
  SSM_PREFIX = "/sechub/integration/"

  print("Parse SSM Params")
  workspace = {}
  print("ssm_client")
  ssm_client = boto3.client('ssm')
  workspace_url = get_param(ssm_client, f'{SSM_PREFIX}{WORKSPACE_NAME}/workspace/url', True)
  workspace["endpoint"] = workspace_url + "api/v5/graphql"
  workspace["access_key"] = get_param(ssm_client, f'{SSM_PREFIX}{WORKSPACE_NAME}/workspace/access_key', True)
  workspace["secret_key"] = get_param(ssm_client, f'{SSM_PREFIX}{WORKSPACE_NAME}/workspace/secret_key', True)
  gql = GraphQl(workspace)

  print("Iterate over events")
  for event_record in event['Records']:
    #receipt_handle = event_record['receiptHandle']
    body = json.loads(event_record['body'])
    msg_body = json.loads(body['Message'])
    msg_time = msg_body["turbot"]["createTimestamp"]
    msg_type = msg_body["notificationType"]
    if msg_type != "control_updated":
      print(f"[INFO] Ignore record - Notification type: {msg_type}")
      continue
    control = msg_body["control"]
    print("Parsing Resource Metadata")
    resource_metadata = control["resource"]["metadata"]
    if "aws" not in resource_metadata:
      print(f"[INFO] Ignore record - Cloud provider not AWS")
      continue
    aws_metadata = resource_metadata["aws"]
    print("Checking if latest Event")
    control_id = control["turbot"]["id"]
    control_state = control["state"]
    curr_control = get_control(gql, control_id)
    if not curr_control:
      print("FILTER: No Control State, Skipping Event")
      continue
    curr_control_state = curr_control["state"]
    resource_akas = curr_control["akas"]
    old_control_state = "TBD"
    if "oldControl" in msg_body:
      old_control_state = msg_body["oldControl"]["state"]
    if control_state != curr_control_state:
      print("FILTER: Control states DO NOT match, Skipping Event")
      print(f"Current State: {curr_control_state} | Event State: {control_state}")
      continue
    if control_state == old_control_state:
      print("FILTER: Control states HAVE NOT changed, Skipping Event")
      print(f"Event State: {control_state} | Old State: {old_control_state}")
      continue
    if control_state not in ["alarm", "ok"]:
      print("FILTER: Control not ALARM or OK, Skipping Event")
      print(f"Event State: {control_state}")
      continue
    if (control_state == "ok") and (old_control_state != "alarm"):
      print("FILTER: Control is OK, but previous control state is not ALARM")
      print(f"Event State: {control_state} | Old State: {old_control_state}")
      continue
    print("FILTER: Control Passes All Filters, Processing...")
    finding = convert_to_asff(msg_time, control, aws_metadata, resource_akas)
    partition = aws_metadata["partition"] if "partition" in aws_metadata else None
    region_name = aws_metadata["regionName"] if "regionName" in aws_metadata else None
    msg_attributes = {
        'account': {
            'DataType': 'String',
            'StringValue': aws_metadata["accountId"]
        },
        'partition': {
            'DataType': 'String',
            'StringValue': partition
        },
        'region': {
            'DataType': 'String',
            'StringValue': region_name
        }
    }
    data = json.dumps(finding)
    print("sqs_client")
    sqs_client = boto3.client('sqs')
    try:
      response = sqs_client.send_message(
        QueueUrl=FINDINGS_QUEUE_URL,
        MessageAttributes=msg_attributes,
        MessageBody=data
      )
      print(f"[SUCCESS] Message sent")
      print(response)
    except ClientError as e:
      print(f'Could not send meessage to: {FINDINGS_QUEUE_URL}.')
      print(e)
