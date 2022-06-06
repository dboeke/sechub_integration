import json
import boto3
import requests

def get_param(ssm_client, param_name, encrypted):
  response = ssm_client.get_parameter(
    Name=param_name,
    WithDecryption=encrypted
  )
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

if __name__ == "__main__":
  filters = {
    "vpc_ingress_rules_watch": [
      "controlTypeId:'tmod:@turbot/aws-vpc-security#/control/types/securityGroupIngressRulesApproved notificationType:control_updated"
    ],
    "s3_bucket_watch": [
      "controlTypeId:'tmod:@turbot/aws-s3#/control/types/bucketLevelPublicAccessBlock','tmod:@turbot/aws-s3#/control/types/bucketEncryptionAtRest' notificationType:control_updated"
    ],
    "iam_role_watch": [
      "controlTypeId:'tmod:@turbot/aws-iam#/control/types/roleActive','tmod:@turbot/aws-iam#/control/types/roleInlinePolicyApproved' notificationType:control_updated"
    ]
  }

  workspace_accounts = {
    "morales": [
      "arn:aws:::133534076130"
    ]
  }

  mutation = '''
    mutation CreateWatch($input: CreateWatchInput!) {
      createWatch(input: $input) {
        filters
        handler
        turbot {
          id
          resourceId
        }
      }
    }
  '''

  SSM_PREFIX = "/sechub/integration/"
  AWS_REGION = "eu-central-1"

  for workspace_name, accounts in workspace_accounts.items():
    workspace = {}
    ssm_client = boto3.client('ssm', region_name=AWS_REGION)
    workspace_url = get_param(ssm_client, f'{SSM_PREFIX}{workspace_name}/workspace/url', False)
    workspace["endpoint"] = "{}/api/v5/graphql".format(workspace_url)
    if workspace_url[-1] == '/':
      workspace["endpoint"] = "{}api/v5/graphql".format(workspace_url)
    workspace["access_key"] = get_param(ssm_client, f'{SSM_PREFIX}{workspace_name}/workspace/access_key', True)
    workspace["secret_key"] = get_param(ssm_client, f'{SSM_PREFIX}{workspace_name}/workspace/secret_key', True)
    gql = GraphQl(workspace)

    for account in accounts:
      print(f"Creating watches for account: {account}")
      for aka, filter in filters.items():
        print(f"Creating {aka} watch")
        vars = {
          "input": {
            "resource": account,
            "action": "tmod:@turbot/firehose-aws-sns#/action/types/router",
            "identity": aka,
            "filters": filter
          }
        }
        response = gql.run_query(mutation, vars)
        print(response)
        print()
