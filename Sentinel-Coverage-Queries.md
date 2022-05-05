# Diagnosing Sentinel connectivity

## SecurityEvents by computer
## Purpose - This will generate a list of all the assets sending Windows Security logs to Sentinel.
```kusto
SecurityEvent | where TimeGenerated > ago(1d) | summarize count() by Computer
```

## Process Creation Windows Event
## Purpose - This will generate a list of all the assets sending Process Creation events including the CommandLine field. The CommandLine field is essential for analysis and correlation. 
```kusto
SecurityEvent | where TimeGenerated > ago(1d) | where EventID == 4688 | where isnotempty(CommandLine) | summarize count() by Computer
```

## Events by computer
## Purpose - This will generate a list of all the assets sending any Windows logs to Sentinel. This will capture hosts that are sending System and Application logs but not Security logs. 
```kusto
Event | where TimeGenerated > ago(1d) | summarize count() by Computer
```

## Logon events
## Purpose - This will generate a list of all the assets sending Windows Logon events.
```kusto
SecurityEvent | where TimeGenerated > ago(7d) | where EventID == 4624 | summarize count() by Computer
```

## Sysmon events
## Purpose - This will generate a list of all the assets sending Windows Sysmon Process Created logs to Sentinel.
```kusto
Event | where Source == "Microsoft-Windows-Sysmon" | where TimeGenerated > ago(1d) |where EventID == 1  | summarize count()
```

## Powershell events
## Purpose - This will generate a list of all the assets sending Windows PowerShell logs to Sentinel.
```kusto
Event | where TimeGenerated > ago(7d) | where Source == "PowerShell" | summarize count()
```

## Kerberos service ticket was requested
## Purpose - This will generate a list of all the assets sending Windows Kerberos related logs to Sentinel. This is an essential log for detecting attacks such as Kerberoasting.
```kusto
SecurityEvent | where TimeGenerated > ago(1d) | where EventID == 4769 | summarize count()
```

## Office Summary
## Purpose - This will generate a list of all the Office services sending logs such as SharePoint and OneDrive.
```kusto
OfficeActivity | summarize count() by RecordType
```

## All security alerts coming in by product name
## Purpose - This will generate a list of all Azure security products sending logs into Sentinel.
```
SecurityAlert | where TimeGenerated > ago(7d) | summarize count() by ProductName
```

## Security events by activity
## Purpose - This will generate a list of all Windows Security logs by thei Event ID and Description. This allows for a check on high volume log sources that may be of low value in a security context.
```kusto
SecurityEvent | summarize count() by Activity
```

## Summary of Billable Logs
## Purpose - This will generate a graph showing a breakdown of logs and their volumes.
```kusto
Usage
| where StartTime >= startofday(ago(31d)) and EndTime < startofday(now())
| where IsBillable == true
| summarize BillableDataGB = sum(Quantity) / 1000. by bin(StartTime, 1d), Solution
| extend Solution = iif(Solution == "SecurityInsights", "AzureSentinel", Solution)
| render columnchart
```

