---
title: "Date.IsLeapYear | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsLeapYear

  
## About  
Returns a logical value indicating whether the year portion of a DateTime value is a leap year.  
  
## Syntax

<pre>  
Date.IsLeapYear(dateTime as nullable datetime) as nullable logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check.|  
  
## Examples  

```powerquery-m
Date.IsLeapYear(DateTime.FromText("2011-01-01")) equals false
```  
  
```powerquery-m 
Date.IsLeapYear(DateTime.FromText("2012-01-01")) equals true  
```  
