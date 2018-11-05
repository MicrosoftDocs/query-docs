---
title: "Date.AddMonths | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.AddMonths

  
## About  
Returns a DateTime value with the month portion incremented by n months.  
  
## Syntax

<pre>   
Date.AddMonths(dateTime as datetime, numberOfMonths as number) as nullable datetime  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add months to.|  
|numberOfMonths|The number of months to add.|  
  
## Remarks  
  
-   It also handles incrementing the year portion of the value as appropriate.  
  
## Examples  
  
```powerquery-m 
Date.AddMonths(DateTime.FromText("2011-02-19"), 5) equals 2011-07-19  
```  
  
```powerquery-m 
Date.AddMonths(DateTime.FromText("2010-12-01"), 2) equals 2011-02-01  
```  
