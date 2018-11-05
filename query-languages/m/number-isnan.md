---
title: "Number.IsNaN | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.IsNaN

  
## About  
Returns true if a value is Number.NaN.  
  
## Syntax

<pre>
Number.IsNaN(value as number) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to evaluate.|  
  
## Examples  
  
```powerquery-m  
Number.IsNaN(1) equals false  
```  
  
```powerquery-m
Number.IsNaN(0/0) equals true  
```  
