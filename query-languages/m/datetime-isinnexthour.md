---
title: "DateTime.IsInNextHour | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextHour

## Syntax

<pre>
DateTime.IsInNextHour(dateTime as any) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value occurs during the next hour, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the hour after the current system time is in the next hour.  
  
```powerquery-m
DateTime.IsInNextHour(DateTime.LocalNow() + #duration(0,1,0,0))  
```  
  
```powerquery-m
Equals: true  
```  
