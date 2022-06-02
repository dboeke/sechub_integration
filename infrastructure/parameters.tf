# params = {
#   workspace_url,
#   workspace_access_key,
#   workspace_secret_key,
# }


resource "aws_ssm_parameter" "workspace_url" {
  for_each  = var.workspaces
  name      = "/sechub/integration/${each.key}/workspace/url"
  type      = "String"
  value     = each.value
}

resource "aws_ssm_parameter" "workspace_access_key" {
  for_each  = var.workspaces
  name      = "/sechub/integration/${each.key}/workspace/access_key"
  type      = "SecureString"
  value     = var.workspace_access_key[each.key]
}

resource "aws_ssm_parameter" "workspace_secret_key" {
  for_each  = var.workspaces
  name      = "/sechub/integration/${each.key}/workspace/secret_key"
  type      = "SecureString"
  value     = var.workspace_secret_key[each.key]
}