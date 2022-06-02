import os
import json
import boto3
import requests
from botocore.exceptions import ClientError

def lambda_handler(event, context):
  print("Parse Lambda Params")
  AWS_REGION = os.environ['AWS_REGION']

  print("Iterate over events")
  for event_record in event['Records']:
    #receipt_handle = event_record['receiptHandle']
    body = json.loads(event_record['body'])
    print("Raw Message:")
    print(body)
    msg_body = json.loads(body['Message'])
    print("Parsed ASFF:")
    print(msg_body)