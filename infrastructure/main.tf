##

data "aws_caller_identity" "current" {}

variable "aws_profile" {
  description = "Enter profile matching your aws cli credentials."
  type        = string
}

variable "aws_region" {
  description = "Enter region for deployment"
  type        = string
}

variable "workspaces" {
  description = "Map of the turbot workspaces"
  type        = map
}

variable "workspace_access_key" {
  description = "Map of the turbot workspace access keys"
  type        = map
}

variable "workspace_secret_key" {
  description = "Map of the turbot workspace secret keys"
  type        = map
}

variable "subnet_ids" {
  description = "List of SubnetIDs for Lambda"
  type        = list(string)
}

variable "security_groups" {
  description = "List of Security Groups to attach to Lambda functions"
  type        = list(string)
}

variable "assume_role_name" {
  description = "Enter name of cross account role for sending security hub issues"
  type        = string
}

variable "assume_role_external_id" {
  description = "Enter external id cross account role for sending security hub issues"
  type        = string
}