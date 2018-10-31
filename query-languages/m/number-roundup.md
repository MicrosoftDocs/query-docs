---
title: "Number.RoundUp | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundUp

  
## About  
Returns the larger integer greater than or equal to a number value.  
  
## Syntax

<pre>
Number.RoundUp(value as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to round up.|  
  
## Examples  
  
```powerquery-m
Number.RoundUp(-1.2) equals -1  
```  
  
```powerquery-m 
Number.RoundUp(1.2) equals 2  
```  
