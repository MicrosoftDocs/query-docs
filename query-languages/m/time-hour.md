---
title: "Time.Hour | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.Hour

  
## About  
Returns an hour value from a DateTime value.  
  
## Syntax

<pre>
Time.Hour(dateTime as datetime) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|dateTime|The DateTime to check against.|  
  
## Example  
  
```powerquery-m  
Time.Hour(DateTime.FromText("12:56:20")) equals 12  
```  
