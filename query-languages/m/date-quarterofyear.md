---
title: "Date.QuarterOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.QuarterOfYear

  
## About  
Returns a number between 1 and 4 for the quarter of the year from a DateTime value.  
  
```  
Date.QuarterOfYear(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Examples  
  
```  
Date.QuarterOfYear(DateTime.FromText("2011-03-21")) equals 1  
```  
  
```  
Date.QuarterOfYear(DateTime.FromText("2011-11-21")) equals 4  
```  
