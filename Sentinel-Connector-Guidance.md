# Microsoft Sentinel Connector Guide
The below guide has been constructed to prioritise connectors and configuration based on cost and complexity. There are several [free data sources](https://docs.microsoft.com/en-us/azure/sentinel/billing?tabs=commitment-tier#free-data-sources) for [Microsoft Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/), however the best approach is to connect as much as you can, then monitor costs and [run queries to understand your data ingestion](https://docs.microsoft.com/en-us/azure/sentinel/billing-monitor-costs#run-queries-to-understand-your-data-ingestion) to reduce your costs where possible.

## High value / low cost connections
These connectors are largely built into the cost of the services they protect, and provide a high value in terms of assets protected.

1. [Connect Azure Active Directory (Azure AD) data](https://docs.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory)
   - [Audit logs, Sign-in logs, Provisioning logs, Risky users logs, Risk detections logs](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/howto-integrate-activity-logs-with-log-analytics#send-logs-to-azure-monitor)
1. [Connect data from Microsoft 365 Defender](https://docs.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender)
   - [DeviceInfo, DeviceNetworkInfo, DeviceProcessEvents, DeviceNetworkEvents, DeviceFileEvents, DeviceRegistryEvents, DeviceLogonEvents, DeviceImageLoadEvents, DeviceEvents, DeviceFileCertificateInfo, EmailAttachmentInfo, EmailEvents, EmailPostDeliveryEvents, EmailUrlInfo](https://docs.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender?tabs=MDE#connect-to-microsoft-365-defender)

## Complex connections

## Potentially high cost connections

## Cost optimisation