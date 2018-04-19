---
title: "Date.AddQuarters | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.AddQuarters

  
## About  
Returns a Date/DateTime/DateTimeZone value incremented by the number of quarters provided. Each quarter is defined as a duration of three months. It also handles incrementing the year potion of the value as appropriate.  
  
```  
Date.AddQuarters(dateTime, quarters as number)  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add quarters to.|  
|quarters|The number of quarters to add.|  
  
## Examples  
  
```  
Date.AddQuarters(DateTime.FromText("2011-02-19"), 1) equals 2011-05-19  
```  
  
```  
Date.AddQuarters(DateTime.FromText("2011-11-30"), 1) equals 2012-02-29  
```  
