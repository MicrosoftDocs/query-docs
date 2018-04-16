---
title: "Time.Hour | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.Hour

  
## About  
Returns an hour value from a DateTime value.  
  
```  
Time.Hour(dateTime as datetime) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Time.Hour(DateTime.FromText("12:56:20")) equals 12  
```  
