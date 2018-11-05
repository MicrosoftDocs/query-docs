---
title: "Duration.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.ToRecord

  
## About  
Returns a record with parts of a Duration value.  
  
## Syntax

<pre>
Duration.ToRecords(duration as duration) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## Example  
  
```powerquery-m
Duration.ToRecord(#duration(2, 5, 55, 20)) equals [Days=2, Hours=5, Minutes=55, Seconds=20]  
```  
