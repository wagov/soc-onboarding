---
Title: "WA SOC Onboarding"
Author: "WA Security Operations Centre"
Company: "github.com/wagov/soc-onboarding"
---

# WA SOC Onboarding Guidance

## 1. Onboarding Templates

When commencing the onboarding process, the WA SOC will provide you with prefilled [Temaplates](https://docs.microsoft.com/en-us/azure/lighthouse/how-to/onboard-customer#create-your-template-manually) that will initiate a [Azure Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse/overview) connection between the customer Azure Tenant and the WA SOC Tenant. Once completed the WA SOC can start to provide SOC servcies to customers.

Dependant on the SOC service tier that the customer have sign onto - It is recommended to onboard to the WA SOC via the following [methods](#2-onboarding-tiers).

## 2. Onboarding Process
----

### Prerequisite

> [Global Admin](https://docs.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#global-administrator) permission required for the Azure Tenant

## 2.1 Tier 0 & Tier 1 Customers
---

Onboarding on the WA SOC as a Tier 0 or Tier 1 customer can be complete quite easily via the [Portal](https://docs.microsoft.com/en-us/azure/lighthouse/overview) method.

**2.1.1** From the Service providers page in the Azure portal, select Server provider offers.

**2.1.2** Near the top of the screen, select the arrow next to Add offer, and then select Add via template.

![service Provider](/images/Service-Provider.png)

**2.1.3** Upload the template by dragging and dropping it, or select Browse for files to find and upload the template.

![Upload Template](/images/Upload-Template.png)

**2.1.4** After you've uploaded your template, select Upload.

**2.1.5** In the Custom deployment screen, review the details that appear. If needed, you can make changes to these location of the template deployment (Australia East is default).

**2.1.6** Select Review and create, then select Create.

## 2.2 Tier 2 Customers
---

**2.2.1** Apply same steps mentioned for [lower tier customers](#21-tier-0--tier-1-customers)

Further information will be provided to customers for further onboarding instructions

> [!NOTE]
> For all customers - It may take up to 15 minutes after your deployment is complete before the updates are reflected in the Azure portal.


## 3. Confirmation of Onboarding

Once the template phase has completed, cusotmers can confirm the onboarding process has finalised by checking the following:

**3.1** Navigate to the Service providers page.

**3.2** Select Service provider offers.

**3.3** Confirm that you can see the WA SOC service offer.

![service Offer](/images/service-offer.png)




