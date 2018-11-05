---
title: "Time.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.ToRecord

  
## About  
Returns a record containing parts of a Date value.  
  
## Syntax

<pre>
Time.ToRecord(time as time) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|time|The time to parse.|  
  
## Example  
  
```powerquery-m
Time.ToRecord(#time(12, 1, 2)) equals [Hour=12, Minute=1, Second=2]  
```  
