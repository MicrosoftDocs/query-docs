---
title: "DateTimeZone.ToUtc | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTimeZone.ToUtc

  
## About  
Returns a DateTime value to the Utc time zone.  
  
## Syntax

<pre>
DateTimeZone.ToUtc(dateTime as datetimezone) as nullable datetimezone  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTimeZone to convert.|  
  
## Example  
  
```powerquery-m
dateTime  = DateTimeZone.FromText("2011-02-20T22:19:27+03:00")  
```  
  
```powerquery-m
utcTime = DateTimeZone.ToUtc(dateTime)equals 2011-02-20T19:19:27+00:00  
```  
