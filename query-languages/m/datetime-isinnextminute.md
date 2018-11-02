---
title: "DateTime.IsInNextMinute | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextMinute

## Syntax

<pre>
DateTime.IsInNextMinute(dateTime as any) as nullable logical  
</pre>

## About  
Indicates whether the given datetime value occurs during the next minute, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the minute after the current system time is in the next minute.  
  
```powerquery-m
DateTime.IsInNextMinute(DateTime.LocalNow() + #duration(0,0,1,0))  
```  
  
```powerquery-m
Equals: true  
```  
