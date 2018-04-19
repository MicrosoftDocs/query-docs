---
title: "Date.AddYears | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.AddYears

  
## About  
Returns a DateTime value with the year portion incremented by n years.  
  
```  
Date.AddYears(dateTime as datetime, years as number) as datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add years to.|  
|years|The number of years to add.|  
  
## Example  
  
```  
Date.AddYears(DateTime.FromText("2011-02-19"), 10) equals 2021-02-19  
```  
