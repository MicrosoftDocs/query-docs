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
  
```  
Date.Month(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to retrieve the month for.|  
  
## Example  
  
```  
Date.Month(DateTime.FromText("2011-02-19")) equals 2  
```  
