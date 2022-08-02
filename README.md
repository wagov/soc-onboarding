# soc-onboarding
WA SOC 2.0 onboarding scripts and documentation

## Onboarding Documentation

To create a set of Azure AD groups, and link them into a parameter json template file, the [lighthouse-onboard.py](lighthouse-onboard.py) can be used. This is designed to be run with a logged in [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli) such as [Azure Cloud Shell](https://shell.azure.com/bash), from which the params.json file can be downloaded.

```bash
# the agencyname_params.json generated below can be downloaded from your cloud shell for further use.
curl https://raw.githubusercontent.com/wagov/soc-onboarding/main/lighthouse-onboard.py | python3 - AGENCYNAME agencyname_params.json
```

## Sentinel Documentation

The handy [Sentinel Connector Guidance](Sentinel-Connector-Guidance.md) can be viewed online or downloaded as a PDF below:

- [Sentinel Connector Guidance (HTML, Online)](https://wagov.github.io/soc-onboarding/Sentinel-Connector-Guidance.html)
- [Sentinel Connector Guidance (PDF)](https://wagov.github.io/soc-onboarding/static/Sentinel-Connector-Guidance.pdf)

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
