---
title: "Date.Year | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.Year

  
## About  
Returns the year from a DateTime value.  
  
```  
Date.Year(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the year for.|  
  
## Example  
  
```  
Date.Year(DateTime.FromText("2011-02-19")) equals 2011  
```  
