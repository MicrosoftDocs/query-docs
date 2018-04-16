---
title: "Time.StartOfHour | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.StartOfHour

  
## About  
Returns the first value of the hour from a time value.  
  
```  
Time.StartOfHour(datetime as datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```  
Time.StartOfHour(#datetime(2013, 4, 5, 1, 3, 45)) equals #datetime(2013, 4, 5, 1, 0, 0)  
```  
