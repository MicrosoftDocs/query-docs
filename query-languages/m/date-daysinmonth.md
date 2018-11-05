---
title: "Date.DaysInMonth | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DaysInMonth

  
## About  
Returns the number of days in the month from a DateTime value.  
  
## Syntax

<pre>  
Date.DaysInMonth(dateTime as datetime) as nullable number  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```powerquery-m  
Date.DaysInMonth(DateTime.FromText("2012-03-01")) equals 31  
```  
