---
Title: "WA SOC Onboarding"
Author: "WA Security Operations Centre"
Company: "github.com/wagov/soc-onboarding"
---
# WA SOC Onboarding Procedure

- [1. Overview](#1-overview)
  - [1.1. Azure Subscription access](#11-azure-subscription-access)
  - [1.2. Microsoft 365 tenant access](#12-microsoft-365-tenant-access)
- [2. Onboarding Process](#2-onboarding-process)
  - [2.1. Prerequisites](#21-prerequisites)
  - [2.2. Microsoft 365 tenant access delegation](#22-microsoft-365-tenant-access-delegation)
    - [2.2.1. Tier 0 Azure AD Group](#221-tier-0-azure-ad-group)
    - [2.2.2. Tier 1 Azure AD Group](#222-tier-1-azure-ad-group)
  - [2.3. Azure Subscription access delegation](#23-azure-subscription-access-delegation)
    - [2.3.1. Azure Lighthouse ARM Deployment](#231-azure-lighthouse-arm-deployment)
- [3. Confirmation of Onboarding](#3-confirmation-of-onboarding)

## 1. Overview

There are 2 delegations of access an operational security team would need to assist a customer with managing their security events and detection rules. Our customer offerings below have been constructed around the type of ongoing access and assistance required:

- **Tier 0 - Monitor:** Ability for automation and analyst accounts to read security incidents, alerts, event data and azure subscription resources.
  - Microsoft 365 Tenant (Azure AD) Role: [Security Reader](https://docs.microsoft.com/en-au/azure/active-directory/roles/permissions-reference#security-reader)
  - Azure Subscription Role: [Reader](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#microsoft-sentinel-reader)
- **Tier 1 - Advisor:** Increased access for analysts to work on security incidents and detection rules ontop of **Tier 0**.
  - Microsoft 365 Tenant (Azure AD) Role: [Security Operator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#security-operator)
  - Azure Subscription Roles: [Reader](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader), [Microsoft Sentinel Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#microsoft-sentinel-contributor), [Security Admin](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#security-admin)

Note for Tier 2 customers, the WA SOC will reach out and complete onboarding activities, including the configuration of [Azure AD Privileged Identity Management](https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-configure) (PIM) on the customer's behalf once initial admin access has been delegated. There are no further steps in this document to follow for Tier 2 customers.

- **Tier 2 - Detect & Respond:** A modern privileged identity management approach to allow for administrative access during incident response and planned changes (security improvements) ontop of **Tier 1**.
  - Microsoft 365 Tenant (Azure AD) Role: [Global Administrator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#global-administrator) via PIM, day to day same as **Tier 1**
  - Azure Subscription Role: [Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#contributor) eligible via PIM, day to day same as **Tier 1**

### 1.1. Azure Subscription access

As part of onboarding, the WA SOC will send the customer a prefilled [Azure Lighthouse ARM Deployment](https://docs.microsoft.com/en-us/azure/lighthouse/how-to/onboard-customer#create-your-template-manually) that can be installed as an **Service provider offer** to initiate an [Azure Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse/overview) connection between the customer Azure Subscription and the WA SOC Tenant. Once completed the WA SOC can delegate relevant permissions to analysts and automation processes via privileged groups in the WA SOC tenant, allowing it to service the customers Azure subscription. This process needs to be undertaken for each subscription the customer would like to delegate access to.

### 1.2. Microsoft 365 tenant access

As part of onboarding, the WA SOC will send the customer a list of analysts (Tier 0 and Tier 1) or privileged approvers (Tier 2) to be delegated specific access in the customers  Azure AD Tenant. This process needs to be undertaken for each Azure AD Tenant the customer would like to delegate access to.

## 2. Onboarding Process

### 2.1. Prerequisites

- [Global Admin](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#global-administrator) permission required for the Azure AD Tenant and associated Azure Subscriptions.
  - [Access to Service provider offers](https://portal.azure.com/#view/Microsoft_Azure_CustomerHub/ServiceProvidersBladeV2/~/providers) in the Azure Portal
  - [Access to Azure Active Directory Groups](https://portal.azure.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/AllGroups) in the Azure Portal

### 2.2. Microsoft 365 tenant access delegation

As a first step invite the `wasoc-analyst-invites.csv` into your [Azure AD directory](https://portal.azure.com/#view/Microsoft_AAD_UsersAndTenants/UserManagementMenuBlade/~/AllUsers).

![Bulk Invite](images/azuread-bulkinvite.png) ![Bulk Invite 2](images/azuread-bulkinvite2.png)

Once thats done [create an Azure AD Group](https://portal.azure.com/#view/Microsoft_AAD_IAM/AddGroupBlade) as per the below templates.

![Create Group](images/azuread-wasocgroup.png)

#### 2.2.1. Tier 0 Azure AD Group

Create an Azure AD group as follows. Any future changes to membership will be requested by the WA SOC.

- **Group type:** Security
- **Group name:** WASOC-T0-Advisor
- **Group description:** WASOC Tier 0 Advisor Access (Security Reader)
- **Azure AD roles can be assigned:** Yes
- **Members:** Each email address imported from `wasoc-analyst-invites.csv`
- **Roles:** [Security Reader](https://docs.microsoft.com/en-au/azure/active-directory/roles/permissions-reference#security-reader)

#### 2.2.2. Tier 1 Azure AD Group

Create an Azure AD group as follows. Any future changes to membership will be requested by the WA SOC.

- **Group type:** Security
- **Group name:** WASOC-T1-Monitor
- **Group description:** WASOC Tier 1 Monitor Access (Security Operator)
- **Azure AD roles can be assigned:** Yes
- **Members:** Each email address imported from `wasoc-analyst-invites.csv`
- **Roles:** [Security Operator](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#security-operator)

### 2.3. Azure Subscription access delegation

The Azure subscription access can be delegated via the [Azure Portal](https://docs.microsoft.com/en-us/azure/lighthouse/overview).

Navigate to the [Azure Lighthouse - Service Providers](https://portal.azure.com/#view/Microsoft_Azure_CustomerHub/ServiceProvidersBladeV2/~/providers) page in the Azure portal, and select the arrow next to Add offer, and then select Add via template.

![service Provider](/images/Service-Provider.png)

#### 2.3.1. Azure Lighthouse ARM Deployment

Browse for the template provided, and click **Upload**. This can be customised to removed unused groups if desired for the customers Tier - please inform the WA SOC of any changes prior to deployment to allow documentation to be updated.

![Upload Template](/images/Upload-Template.png)
Review the custom deployment details and ensure the location is Australia East, then click **Review and create** then click **Create**.

## 3. Confirmation of Onboarding

Once the template phase has completed, cusotmers can confirm the onboarding process has finalised by navigating to the [Azure Lighthouse - Service Providers](https://portal.azure.com/#view/Microsoft_Azure_CustomerHub/ServiceProvidersBladeV2/~/providers) page and confirming you can see the **WA SOC - Security Insights** service offer.

![service Offer](/images/service-offer.png)
