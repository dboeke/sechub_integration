

resource "aws_sns_topic" "raw_alarms_topic" {
  for_each          = var.workspaces
  name              = "${each.key}_firehose_raw_alarms"
  kms_master_key_id = "alias/aws/sns"
}

resource "aws_sqs_queue" "raw_alarms_queue" {
  for_each                   = var.workspaces
  name                       = "${each.key}_firehose_raw_alarms_queue"
  sqs_managed_sse_enabled    = true
  delay_seconds              = 1
  receive_wait_time_seconds  = 10
  visibility_timeout_seconds = 150
  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.raw_alarms_dlq[each.key].arn
    maxReceiveCount     = 4
  })
  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue",
    sourceQueueArns   = [aws_sqs_queue.raw_alarms_dlq[each.key].arn]
  })
}

resource "aws_sqs_queue_policy" "raw_alarms_queue_policy" {
  for_each  = var.workspaces
  queue_url = aws_sqs_queue.raw_alarms_queue[each.key].id
  policy = <<-POLICY
    {
      "Version": "2012-10-17",
      "Id": "sqspolicy",
      "Statement": [
        {
          "Sid": "AllowSNS",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "sqs:SendMessage",
          "Resource": "${aws_sqs_queue.raw_alarms_queue[each.key].arn}",
          "Condition": {
            "ArnEquals": {
              "aws:SourceArn": "${aws_sns_topic.raw_alarms_topic[each.key].arn}"
            }
          }
        }
      ]
    }
    POLICY
}

resource "aws_sqs_queue" "raw_alarms_dlq" {
  for_each                = var.workspaces
  name                    = "${each.key}_firehose_raw_alarms_dlq"
  sqs_managed_sse_enabled = true
}

resource "aws_sns_topic_subscription" "raw_events_subscription" {
  for_each  = var.workspaces
  topic_arn = aws_sns_topic.raw_alarms_topic[each.key].arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.raw_alarms_queue[each.key].arn
}
