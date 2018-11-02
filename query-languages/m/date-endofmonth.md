---
title: "Date.EndOfMonth | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.EndOfMonth

  
## About  
Returns a DateTime value for the end of the month.  
  
## Syntax

<pre>  
Date.EndOfMonth(dateTime as nullable datetime) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the month.  
  
-   The timezone information is persisted.  
  
## Example  
  
```powerquery-m 
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Date.EndOfMonth(dateTime) equals 2011-02-28T23:59:59-08:00  
```  
