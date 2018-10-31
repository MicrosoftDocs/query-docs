---
title: "DateTime.IsInPreviousSecond | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousSecond

## Syntax

<pre>
DateTime.IsInPreviousSecond(dateTime as any) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value occurs during the previous second, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the second before the current system time is in the previous second.  
  
```powerquery-m
DateTime.IsInPreviousSecond(DateTime.FixedLocalNow() - #duration(0,0,0,1))  
```  
  
```powerquery-m
Equals: true  
```  
