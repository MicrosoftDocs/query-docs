---
title: "Time.Minute | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.Minute

  
## About  
Returns a minute value from a DateTime value.  
  
## Syntax

<pre> 
Time.Minute(dateTime as datetime) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```powerquery-m 
Time.Minute(DateTime.FromText("12:56:20")) equals 56  
```  
