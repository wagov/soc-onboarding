# Microsoft Sentinel Connector Guide
The below guide has been constructed to prioritise connectors and configuration based on cost and complexity. There are several [free data sources](https://docs.microsoft.com/en-us/azure/sentinel/billing?tabs=commitment-tier#free-data-sources) for [Microsoft Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/), however the best approach is to connect as much as you can, then monitor costs and [run queries to understand your data ingestion](https://docs.microsoft.com/en-us/azure/sentinel/billing-monitor-costs#run-queries-to-understand-your-data-ingestion) to reduce your costs where possible.

## High value / low cost connections
These connectors are largely built into the cost of the services they protect, and provide a high value in terms of assets protected.

1. [Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory) - Identity management logs
   - [Audit logs, Sign-in logs, Provisioning logs, Risky users logs, Risk detections logs](https://docs.microsoft.com/en-us/azure/active-directory/reports-monitoring/howto-integrate-activity-logs-with-log-analytics#send-logs-to-azure-monitor)
1. [Microsoft 365 Defender](https://docs.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender) - Devices (Endpoints, Servers) and Exchange Online events
   - [DeviceInfo, DeviceNetworkInfo, DeviceProcessEvents, DeviceNetworkEvents, DeviceFileEvents, DeviceRegistryEvents, DeviceLogonEvents, DeviceImageLoadEvents, DeviceEvents, DeviceFileCertificateInfo, EmailAttachmentInfo, EmailEvents, EmailPostDeliveryEvents, EmailUrlInfo](https://docs.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender?tabs=MDE#connect-to-microsoft-365-defender)

   - Windows, macOS and Linux end-user devices & servers should be onboarded into Microsoft 365 Defender for Endpoint unless they are separately sending the above data to Sentinel via another connector (e.g. [Microsoft Defender for Cloud](https://docs.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) or [Container Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview))
     - [Windows devices in Defender for Endpoint](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/configure-endpoints?view=o365-worldwide) - Windows 7+, Windows Server 2008 R2+
     - [Defender for Endpoint on Mac](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-endpoint-mac?view=o365-worldwide) - macOS 10.15+ (Catalina)
     - [Defender for Endpoint on Linux](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/microsoft-defender-endpoint-linux?view=o365-worldwide) - Debian 9+, Ubuntu 16.04+, RHEL6+, SLES12+, CentOS6+, OEL7+, Fedora33+
        
     This is the lowest cost way per device to get baseline monitoring in place.


## Complex connections
These are good for querying manually, however most require some work to normalise using ... to be incorporated into automatic incident generation using standard Sentinel Rules.

1. [Logstash to connect data sources to Microsoft Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/connect-logstash) - For third party platforms without microsoft documented connection guidance, this is the best integration option.
1. [CEF-formatted logs from your device or appliance](https://docs.microsoft.com/en-us/azure/sentinel/connect-common-event-format)
1. [Linux-based sources using Syslog](https://docs.microsoft.com/en-us/azure/sentinel/connect-syslog)

## Potentially high cost connections
1. TODO: Network Firewalls and Web Application Firewalls
1. [Microsoft Defender for Cloud](https://docs.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) - If possible [Enable all Microsoft Defender plans](https://docs.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security#to-enable-enhanced-security-features-on-your-subscriptions-and-workspaces)
1. [Container Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview) - Centrally monitor [Kubernetes cluster performance](https://docs.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-analyze) and [query logs](https://docs.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-log-query)

## Cost optimisation

Microsoft Sentinel has builtin [queries to understand your data ingestion](https://docs.microsoft.com/en-us/azure/sentinel/billing-monitor-costs#run-queries-to-understand-your-data-ingestion) at a per table level. To get further granularity you can look at specific devices sending a lot of data using [additional usage queries](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-insights-overview#additional-usage-queries) or directly run manual queries from [Investigate your Log Analytics usage](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/manage-cost-storage#investigate-your-log-analytics-usage).