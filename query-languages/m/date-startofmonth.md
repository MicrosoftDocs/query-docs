---
title: "Date.StartOfMonth | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.StartOfMonth

  
## About  
Returns a DateTime value representing the start of the month.  
  
```  
Date.StartOfMonth(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the month.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");  
Date.StartOfMonth(dateTime) equals 2011-02-01T00:00:00-08:00  
```  
