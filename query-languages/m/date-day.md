---
title: "Date.Day | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.Day

  
## About  
Returns the day for a DateTime value.  
  
## Syntax

<pre> 
Date.Day(dateTime as datetime) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the day for.|  
  
## Example  
  
```powerquery-m 
Date.Day(DateTime.FromText("2011-02-19")) equals 19  
```  
