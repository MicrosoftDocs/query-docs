---
title: "Date.EndOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.EndOfYear

  
## About  
Returns a DateTime value for the end of the year.  
  
## Syntax

<pre> 
Date.EndOfYear(dateTime as nullable datetime) as nullable datetime  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the year.  
  
-   The timezone information is persisted.  
  
## Example  
  
```powerquery-m  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Date.EndOfYear(dateTime) equals 2011-12-31T23:59:59-08:00  
```  
