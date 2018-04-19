---
title: "DateTime.Date | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.Date

  
## About  
Returns a date part from a DateTime value  
  
```  
DateTime.Date(dateTime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to parse.|  
  
## Example  
  
```  
DateTime.Date(#datetime(2010, 5, 4, 6, 5, 4)) equals #date(2010, 5, 4)  
```  
