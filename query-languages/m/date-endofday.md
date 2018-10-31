---
title: "Date.EndOfDay | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.EndOfDay

  
## About  
Returns a DateTime value for the end of the day.  
  
## Syntax

<pre>  
Date.EndOfDay(dateTime as nullable datetime) as nullable datetime  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Remarks  
  
-   The date and time portions are reset to their initial values for the day.  
  
-   The timezone information is persisted.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m  
dateTime = DateTimeZone.FromText("2011-02-21T12:30:00-08:00");  
Date.EndOfDay(dateTime) equals 2011-02-21T23:59:590-08:00  
```  
  
## Parameter values  
The following day values can be used **DateTime** functions.  
  
**Day**  
  
|Day|Value|  
|-------|---------|  
|Day.Sunday|0|  
|Day.Monday|1|  
|Day.Tuesday|2|  
|Day.Wednesday|3|  
|Day.Thursday|4|  
|Day.Friday|5|  
|Day.Saturday|6|  
  
