---
title: "DateTime.IsInPreviousNSeconds | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousNSeconds

## Syntax

<pre>
DateTime.IsInPreviousNSeconds(dateTime as any, seconds as number) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value occurs during the previous number of seconds, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
|seconds: The number of seconds.|  
  
### Example 1  
Determine if the second before the current system time is in the previous two seconds.  
  
```powerquery-m
DateTime.IsInPreviousNSeconds(DateTime.FixedLocalNow() - #duration(0,0,0,2), 2)  
```  
  
```powerquery-m
Equals: true  
```  
