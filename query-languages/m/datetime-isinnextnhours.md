---
title: "DateTime.IsInNextNHours | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextNHours

## Syntax

<pre>
DateTime.IsInNextNHours(dateTime as any, hours as number) as nullable logical  
</pre>

## About  
Indicates whether the given datetime value occurs during the next number of hours, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
|hours: The number of hours.|  
  
### Example 1  
Determine if the hour after the current system time is in the next two hours.  
  
```powerquery-m 
DateTime.IsInNextNHours(DateTime.LocalNow() + #duration(0,2,0,0), 2)  
```  
  
```powerquery-m 
Equals: true  
```  
