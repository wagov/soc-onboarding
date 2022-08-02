#!/usr/bin/env python3
import sys, json
from string import Template
from subprocess import check_output

if __name__ == "__main__":
    """
    Prereqs: Run scoped to the tenant and subscription that contains the Azure AD directory, and is intended to be the parent lighthouse instance for the destination tenant.
    Usage: ./lighthouse-onboard.py CODENAME codename-params.json

    The above will create templated groups in Azure AD and generate a lighthouse params file that can be deployed to the customers
    """
    agency = sys.argv[1]
    params = {
        "mssptenantid": json.loads(check_output(["az", "account", "show"]))[
            "homeTenantId"
        ],
        "offername": "WASOC - Security Insights",
    }

    group_prefix = "WASOC"
    group_suffixes = {
        "advisor": "T0-Advisor",
        "monitor": "T1-Monitor",
        "admin": "T2-Admin",
        "approver": "T2-Admin-Approvers",
    }

    print(f"Creating and checking groups for {agency} onboarding...")

    params_template = Template(
        """
    {
        "$$schema": "https://schema.management.azure.com/schemas/2018-05-01/subscriptionDeploymentParameters.json#",
        "contentVersion": "1.0.0.0",
        "parameters": {
            "mspOfferName": {
                "value": "$offername"
            },
            "mspOfferDescription": {
                "value": "$offername"
            },
            "managedByTenantId": {
                "value": "$mssptenantid"
            },
            "authorizations": {
                "value": [
                    {
                        "principalId": "$advisorid",
                        "principalIdDisplayName": "$advisorgroup",
                        "roleDefinitionId": "acdd72a7-3385-48ef-bd42-f606fba81ae7"
                    },
                    {
                        "principalId": "$monitorid",
                        "principalIdDisplayName": "$monitorgroup",
                        "roleDefinitionId": "acdd72a7-3385-48ef-bd42-f606fba81ae7"
                    },
                    {
                        "principalId": "$monitorid",
                        "principalIdDisplayName": "$monitorgroup",
                        "roleDefinitionId": "ab8e14d6-4a74-4a29-9ba8-549422addade"
                    },
                    {
                        "principalId": "$monitorid",
                        "principalIdDisplayName": "$monitorgroup",
                        "roleDefinitionId": "fb1c8493-542b-48eb-b624-b4c8fea62acd"
                    }
                    
                ]
            },
            "eligibleAuthorizations":{
                "value": [ 
                    { 
                            "justInTimeAccessPolicy": { 
                                "multiFactorAuthProvider": "Azure", 
                                "maximumActivationDuration": "PT4H",
                                "managedByTenantApprovers": [ 
                                    { 
                                        "principalId": "$approverid", 
                                        "principalIdDisplayName": "$approvergroup" 
                                    } 
                                ] 
                            },
                            "principalId": "$adminid", 
                            "principalIdDisplayName": "$admingroup",
                            "roleDefinitionId": "b24988ac-6180-42a0-ab88-20f7382dd24c"  
                    }
                ]    
            }
        }
    }
    """
    )

    for role, suffix in group_suffixes.items():
        name = f"{group_prefix}-{agency}-{suffix}"
        existing = json.loads(
            check_output(
                [
                    "az",
                    "ad",
                    "group",
                    "list",
                    "--filter",
                    f"displayName eq '{name}'",
                    "-o",
                    "json",
                ]
            )
        )
        if len(existing) == 0:
            group = json.loads(
                check_output(
                    [
                        "az",
                        "ad",
                        "group",
                        "create",
                        "--display-name",
                        name,
                        "--mail-nickname",
                        name,
                        "-o",
                        "json",
                    ]
                )
            )
        else:
            group = existing[0]
        params[f"{role}group"] = name
        params[f"{role}id"] = group["id"]
    
    print("Generated parameters short form below:")
    print(json.dumps(params, indent=2))

    params_json = json.loads(params_template.substitute(params))

    if len(sys.argv) > 2:
        json.dump(params_json, open(sys.argv[2], "w"), indent=2)
    else:
        print(json.dumps(params_json, indent=2))
