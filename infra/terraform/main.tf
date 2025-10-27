terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  required_version = ">= 1.3.0"
}

provider "azurerm" {
  features {}
}

variable "location" {
  default = "East US"
}

variable "resource_group_name" {
  default = "neurosentinel-rg"
}

resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_app_service_plan" "neurosentinel_plan" {
  name                = "neurosentinel-plan"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  kind                = "Linux"
  reserved            = true

  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "neurosentinel_app" {
  name                = "neurosentinel-app"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.neurosentinel_plan.id

  site_config {
    linux_fx_version = "DOCKER|yourdockerhubusername/neurosentinel:latest"
    always_on        = true
  }

  app_settings = {
    "WEBSITES_PORT"     = "8000"
    "ENVIRONMENT"       = "Production"
    "DOCKER_ENABLE_CI"  = "true"
  }
}

resource "azurerm_key_vault" "neurosentinel_kv" {
  name                        = "neurosentinel-kv"
  location                    = azurerm_resource_group.main.location
  resource_group_name         = azurerm_resource_group.main.name
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  sku_name                    = "standard"
  purge_protection_enabled    = true
  soft_delete_retention_days  = 7

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id

    secret_permissions = [
      "get",
      "set",
      "list",
      "delete"
    ]
  }
}

data "azurerm_client_config" "current" {}
