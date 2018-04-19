---
title: "Time.Minute | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.Minute

  
## About  
Returns a minute value from a DateTime value.  
  
```  
Time.Minute(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Time.Minute(DateTime.FromText("12:56:20")) equals 56  
```  
