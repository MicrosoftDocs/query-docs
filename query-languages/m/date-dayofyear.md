---
title: "Date.DayOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DayOfYear

  
## About  
Returns a number that represents the day of the year from a DateTime value.  
  
## Syntax

<pre>  
Date.DayOfYear(dateTime as datetime) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Examples  
  
```powerquery-m  
Date.DayOfYear(DateTime.FromText("2011-03-01")) equals 60  
```  
  
```powerquery-m  
Date.DayOfYear(DateTime.FromText("2012-03-01")) equals 61  
```  
