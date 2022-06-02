resource "aws_iam_role" "lambda_function_execution_role" {
  name               = "sechub_integration_lambda_execution_role"
  path               = "/"
  description        = "Allows Lambda Function to call AWS services on your behalf."
  assume_role_policy = <<-EOF
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Service": "lambda.amazonaws.com"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    EOF
}

resource "aws_iam_role_policy_attachment" "lambda_role_policy_attachment" {
  role       = aws_iam_role.lambda_function_execution_role.name
  policy_arn = aws_iam_policy.lambda_execution_policy.arn
}

resource "aws_iam_policy" "lambda_execution_policy" {
  name        = "lambda_logging"
  path        = "/"
  description = "IAM policy for logging from a lambda"

  policy = <<-POLICY
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "sqs:SendMessage",
            "sqs:DeleteMessage",
            "sqs:ChangeMessageVisibility",
            "sqs:ReceiveMessage",
            "sqs:TagQueue",
            "sqs:UntagQueue",
            "sqs:PurgeQueue",
            "sqs:GetQ*",
            "sqs:GetQueueAttributes",
            "logs:CreateLogGroup",
            "logs:CreateLogStream",
            "logs:PutLogEvents",
            "sts:AssumeRole",
            "securityhub:UpdateFindings",
            "securityhub:GetFindings",
            "securityhub:BatchUpdateFindings",
            "securityhub:BatchImportFindings",
            "ec2:CreateNetworkInterface",
            "ec2:DescribeNetworkInterfaces",
            "ec2:DeleteNetworkInterface",
            "ec2:AssignPrivateIpAddresses",
            "ec2:UnassignPrivateIpAddresses",
            "ssm:Get*",
            "ssm:Desc*",
            "ssm:List*",
            "kms:Decrypt",
            "kms:List*",
            "kms:Encrypt",
            "kms:Desc*"
          ],
          "Resource": "*"
        }
      ]
    }
POLICY
}

resource "aws_lambda_function" "lambda_filter_functions" {
  for_each         = var.workspaces
  role             = aws_iam_role.lambda_function_execution_role.arn
  handler          = "filter_function.lambda_handler"
  runtime          = "python3.9"
  filename         = "lambdas.zip"
  function_name    = "sechub_integration_${each.key}_filter_function"
  source_code_hash = filebase64sha256("lambdas.zip")
  timeout          = 120
  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_groups
  }
  environment {
    variables = {
      WORKSPACE_NAME = each.key
      FINDINGS_QUEUE_URL = aws_sqs_queue.findings_queue.url
    }
  }
}

resource "aws_lambda_event_source_mapping" "filter_function_to_sqs" {
  for_each         = var.workspaces
  event_source_arn = aws_sqs_queue.raw_alarms_queue[each.key].arn
  function_name    = aws_lambda_function.lambda_filter_functions[each.key].arn
  batch_size       = 10
}

resource "aws_lambda_function" "lambda_sechub_function" {
  role             = aws_iam_role.lambda_function_execution_role.arn
  handler          = "sechub_function.lambda_handler"
  runtime          = "python3.9"
  filename         = "lambdas.zip"
  function_name    = "sechub_integration_sechub_function"
  source_code_hash = filebase64sha256("lambdas.zip")
  timeout          = 30
  environment {
    variables = {
      foo = "bar"
    }
  }
}

resource "aws_lambda_event_source_mapping" "sechub_function_to_sqs" {
  for_each         = var.workspaces
  event_source_arn = aws_sqs_queue.findings_queue.arn
  function_name    = aws_lambda_function.lambda_sechub_function.arn
  batch_size       = 1
}