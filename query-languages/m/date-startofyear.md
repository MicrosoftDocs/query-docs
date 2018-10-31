---
title: "Date.StartOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.StartOfYear

  
## About  
Returns a DateTime value representing the start of the year.  
  
## Syntax

<pre>
Date.StartOfYear(dateTime as nullable datetime) as nullable datetime  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the year.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
dateTime=DateTimeZone.FromText("2011-02-21T12:30:00-08:00")   
Date.StartOfYear(dateTime) equals 2011-01-01T00:00:00-08:00  
```  
