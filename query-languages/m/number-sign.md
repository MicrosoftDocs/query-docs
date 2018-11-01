---
title: "Number.Sign | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Sign

  
## About  
Returns 1 for positive numbers, -1 for negative numbers or 0 for zero.  
  
## Syntax

<pre>
Number.Sign(number as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|Number to evaluate.|  
  
## Examples  
  
```powerquery-m
Number.Sign(-1) equals -1  
```  
  
```powerquery-m
Number.Sign(1) equals 1  
```  
