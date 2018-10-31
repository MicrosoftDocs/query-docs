---
title: "DateTime.IsInPreviousMinute | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousMinute

## Syntax

<pre>
DateTime.IsInPreviousMinute(dateTime as any) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value occurs during the previous minute, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the minute before the current system time is in the previous minute.  
  
```powerquery-m
DateTime.IsInPreviousMinute(DateTime.LocalNow() - #duration(0,0,1,0))  
```  
  
```powerquery-m
Equals: true  
```  
