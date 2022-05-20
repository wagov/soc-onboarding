# soc-onboarding
WA SOC 2.0 onboarding scripts and documentation

## Target Architecture

This repository should contains a bootstrap ARM template and script to launch an ACI instance under a managed identity which uses the `mcr.microsoft.com/azure-cli` container to undertake a sequence of azure cli tasks to complete a full onboarding/connection process.

In scope:
- https://docs.microsoft.com/en-us/azure/lighthouse/how-to/onboard-customer#azure-cli
- https://docs.microsoft.com/en-us/cli/azure/sentinel/alert-rule?view=azure-cli-latest
- https://docs.microsoft.com/en-us/cli/azure/sentinel/data-connector?view=azure-cli-latest
- https://docs.microsoft.com/en-us/microsoft-365/security/defender/mssp-access?view=o365-worldwide
  - https://docs.microsoft.com/en-us/azure/active-directory/privileged-identity-management/pim-how-to-change-default-settings#require-approval-to-activate

Out of scope
- https://docs.microsoft.com/en-us/microsoft-365/lighthouse/m365-lighthouse-overview?view=o365-worldwide
