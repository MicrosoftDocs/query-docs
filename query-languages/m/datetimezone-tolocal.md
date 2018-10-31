---
title: "DateTimeZone.ToLocal | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.ToLocal

  
## About  
Returns a DateTime value from the local time zone.  
  
## Syntax

<pre>
DateTimeZone.ToLocal(dateTime as datetimezone) as nullable datetimezone  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to convert.|  
  
## Example  
  
```powerquery-m
//assuming local as PST   
dateTime  = DateTimeZone.FromText("2011-02-20T22:19:27+03:00")  
localTime=DateTimeZone.ToLocal(dateTime) equals 2011-02-20T11:19:27-08:00  
```  
