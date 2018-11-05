---
title: "DateTime.IsInPreviousHour | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousHour

## Syntax

<pre>
DateTime.IsInPreviousHour(dateTime as any) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value occurs during the previous hour, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the hour before the current system time is in the previous hour.  
  
```powerquery-m
DateTime.IsInPreviousHour(DateTime.LocalNow() - #duration(0,1,0,0))  
```  
  
```powerquery-m
Equals: true  
```  
