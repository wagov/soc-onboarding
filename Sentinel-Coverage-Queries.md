# Diagnosing Sentinel connectivity

## SecurityEvents coming in by computer 
```kusto
SecurityEvent | where TimeGenerated > ago(1d) | summarize count() by Computer
```

## Process creation Windows Event
```kusto
SecurityEvent | where TimeGenerated > ago(1d) | where EventID == 4688 | where isnotempty(CommandLine) | summarize count() by Computer
```

## Events by computer
```kusto
Event | where TimeGenerated > ago(1d) | summarize count() by Computer
```

## logon events
```kusto
SecurityEvent | where TimeGenerated > ago(7d) | where EventID == 4624 | summarize count() by Computer
```

## Powershell captured
```kusto
Event | where TimeGenerated > ago(7d) | where Source == "PowerShell" | summarize count()
```

## Kerberos service ticket was requested
```kusto
SecurityEvent | where TimeGenerated > ago(1d) | where EventID == 4769 | summarize count()
```

## Office activity check
```kusto
OfficeActivity | summarize count() by RecordType
```

## All security alerts coming in by product name
```
SecurityAlert
| where TimeGenerated > ago(7d)
| summarize count() by ProductName
```