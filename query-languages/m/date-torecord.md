---
title: "Date.ToRecord | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.ToRecord

  
## About  
Returns a record containing parts of a Date value.  
  
## Syntax

<pre>
Date.ToRecord(date as date) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|date|The Date to parse.|  
  
## Example  
  
```powerquery-m
Date.ToRecord(#date(2013, 1, 1) equals [Year=2013,Month=1,Day=1]  
```  
