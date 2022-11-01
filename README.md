# soc-onboarding

WA SOC 2.0 onboarding scripts and documentation

## Onboarding Documentation

To create a set of Azure AD groups, and create an associated lighthouse arm template, the [lighthouse-onboard.py](lighthouse-onboard.py) can be used. This is designed to be run with a logged in [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli) such as [Azure Cloud Shell](https://shell.azure.com/bash), from which the lighthouse arm template json file can be downloaded.

```bash
# the agencyname_lighthouse_arm.json generated below can be downloaded from your cloud shell for further use.
curl https://raw.githubusercontent.com/wagov/soc-onboarding/main/lighthouse-onboard.py | python3 - AGENCYNAME agencyname_lighthouse_arm.json
```

## Sentinel Documentation

The handy [Sentinel Connector Guidance](https://wagov.github.io/wasocshared/#/onboarding/sentinel-guidance.md) can be viewed online, and printed to a PDF using your browser.