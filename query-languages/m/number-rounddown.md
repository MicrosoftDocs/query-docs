---
title: "Number.RoundDown | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundDown

  
## About  
Returns the largest integer less than or equal to a number value.  
  
## Syntax

<pre>
Number.RoundDown(value as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round down.|  
  
## Examples  
  
```powerquery-m
Number.RoundDown(-1.2) equals -2  
```  
  
```powerquery-m
Number.RoundDown(1.2) equals 1  
```  
