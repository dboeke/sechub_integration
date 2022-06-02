
resource "aws_sqs_queue" "findings_queue" {
  name                       = "security_hub_findings_queue"
  sqs_managed_sse_enabled    = true
  delay_seconds              = 0
  receive_wait_time_seconds  = 10
  visibility_timeout_seconds = 30
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.findings_dlq.arn
    maxReceiveCount     = 4
  })
  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue",
    sourceQueueArns   = [aws_sqs_queue.findings_dlq.arn]
  })
}

resource "aws_sqs_queue" "findings_dlq" {
  name                    = "security_hub_findings_dlq"
  sqs_managed_sse_enabled = true
}
