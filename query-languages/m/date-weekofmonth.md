---
title: "Date.WeekOfMonth | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.WeekOfMonth

  
## About  
Returns a number for the count of week in the current month.  
  
## Syntax

<pre>
Date.WeekOfMonth(dateTime as datetime) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The **DateTime** to check against.|  
  
## Example  
  
```powerquery-m 
Date.WeekOfMonth(DateTime.FromText("2011-08-30")) equals 5  
```  
