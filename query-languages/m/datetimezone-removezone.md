---
title: "DateTimeZone.RemoveZone | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.RemoveZone

  
## About  
Returns a datetime value with the zone information removed from the input datetimezone value.  
  
## Syntax

<pre>
DateTimeZone.RemoveZone(dateTimeZone as datetimezone) as nullable datetime  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTimeZone|The DateTimeZone to modify.|  
  
## Example  
  
```powerquery-m
DateTimeZone.RemoveZone(#datetimezone(2010, 5, 4, 14, 5, 5, 8, 0)) equals #datetime(2010, 5, 4, 14, 5, 5)  
```  
