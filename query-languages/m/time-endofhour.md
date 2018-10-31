---
title: "Time.EndOfHour | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.EndOfHour

  
## About  
Returns a DateTime value from the end of the hour.  
  
## Syntax

<pre>
Time.EndOfHour(dateTime as datetime) as nullable datetime  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The time portion is reset to its terminating values for the hour.  
  
-   The timezone information is persisted.  
  
## Example  
  
```powerquery-m
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");   
Time.EndOfHour(dateTime) equals 2011-02-21T12:59:59-08:00  
```  
