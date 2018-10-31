---
title: "Date.Month | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.Month

  
## About  
Returns the month from a DateTime value.  
  
## Syntax

<pre>
Date.Month(dateTime as datetime) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the month for.|  
  
## Example  
  
```powerquery-m
Date.Month(DateTime.FromText("2011-02-19")) equals 2  
```  
