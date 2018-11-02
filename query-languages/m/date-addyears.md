---
title: "Date.AddYears | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.AddYears

  
## About  
Returns a DateTime value with the year portion incremented by n years.  
  

## Syntax

<pre> 
Date.AddYears(dateTime as datetime, years as number) as datetime  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to add years to.|  
|years|The number of years to add.|  
  
## Example  
  

```powerquery-m  
Date.AddYears(DateTime.FromText("2011-02-19"), 10) equals 2021-02-19  
```  
