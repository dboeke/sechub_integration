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

def lambda_handler(event, context):
  print("Parse Lambda Params")
  AWS_REGION = os.environ['AWS_REGION']
  SSM_PREFIX = "/sechub/integration"
  print("Parse SSM Params")
  print("ssm_client")
  ssm_client = boto3.client('ssm')
  role_name = get_param(ssm_client, f'{SSM_PREFIX}/siemens/role/name', False)
  role_ext_id = get_param(ssm_client, f'{SSM_PREFIX}/siemens/role/externalid', True)

  print("Iterate over events")
  for event_record in event['Records']:
    #receipt_handle = event_record['receiptHandle']
    asff_message = json.loads(event_record['body'])
    print("Parsed ASFF:")
    account_id = asff_message['AwsAccountId']
    sts_client = boto3.client('sts')
    print(f"Get Assume role creds for: {role_name}")
    sts_creds = sts_client.assume_role(
      RoleArn=f'arn:aws:iam::{account_id}:role/{role_name}',
      ExternalId=role_ext_id,
      RoleSessionName='TurbotSecurityHubReporting'
    )
    print(f"Assuming secuirty hub reporting role in target account")
    sechub_report_client = boto3.client(
      'securityhub', 
      aws_access_key_id=sts_creds['Credentials']['AccessKeyId'],
      aws_secret_access_key=sts_creds['Credentials']['SecretAccessKey'], 
      aws_session_token=sts_creds['Credentials']['SessionToken'],
      region_name=AWS_REGION
    )
    print(asff_message)
    print("Parsing Finding")
    if asff_message['Title'].split(":")[0].lower() == "ok":
      print(f"Update finding")
      response = sechub_report_client.batch_update_findings(
        FindingIdentifiers=[
          {
            'Id': asff_message['Id'],
            'ProductArn': asff_message['ProductArn']
          },
        ],
        Note={
          'Text': asff_message['Description'],
          'UpdatedBy': 'string'
        },
        Severity={
          'Product': 0,
          'Label': 'INFORMATIONAL'
        },
        Confidence=100,
        Types=asff_message['Types'],
        Workflow={
            'Status': 'RESOLVED'
        }
    )
    else:
      print(f"Reporting finding")
      response = sechub_report_client.batch_import_findings(
        Findings=[asff_message]
      )
    print("Findings sent, response:")
    print(response)