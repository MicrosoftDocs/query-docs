---
title: "Date.IsLeapYear | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsLeapYear

  
## About  
Returns a logical value indicating whether the year portion of a DateTime value is a leap year.  
  
```  
Date.IsLeapYear(dateTime as nullable datetime) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check.|  
  
## Examples  
`Date.IsLeapYear(DateTime.FromText("2011-01-01")) equals false`  
  
```  
Date.IsLeapYear(DateTime.FromText("2012-01-01")) equals true  
```  
