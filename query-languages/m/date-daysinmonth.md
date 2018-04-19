---
title: "Date.DaysInMonth | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DaysInMonth

  
## About  
Returns the number of days in the month from a DateTime value.  
  
```  
Date.DaysInMonth(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Date.DaysInMonth(DateTime.FromText("2012-03-01")) equals 31  
```  
