---
title: "DateTime.AddZone | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.AddZone

  
## About  
Adds the timezonehours as an offset to the input datetime value and returns a new datetimezone value.  
  
## Syntax

<pre>
DateTime.AddZone(dateTime as nullable datetime, timezoneHours as number, optional timezoneMinutes as nullable number) as nullable datetimezone  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|A DateTime to modify.|  
|timezoneHours|The hours to add.|  
|optional timezoneMinutes|The minuts to add.|  
  
## Example  
  
```powerquery-m
DateTime.AddZone(#datetime(2010, 5, 4, 6, 5, 5), 8) equals #datetimezone(2010, 5, 4, 6, 5, 5, 8, 0)  
```  
