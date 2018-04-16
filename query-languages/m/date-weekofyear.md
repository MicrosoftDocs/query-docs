---
title: "Date.WeekOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.WeekOfYear

  
## About  
Returns a number for the count of week in the current year.  
  
```  
Date.WeekOfYear(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Date.WeekOfYear(DateTime.FromText("2011-02-21")) equals 8  
```  
