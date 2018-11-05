---
title: "Number.Exp | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Exp

  
## About  
Returns a number representing *e* raised to a power.  
  
## Syntax

<pre>
Number.Exp(number as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|A number for which the exponential function is to be calculated. If number is null,  Number.Exp returns null.|  
  
## Examples  
  
```powerquery-m
Number.Exp(0) equals 1  
```  
  
```powerquery-m 
Number.Exp(3) equals 20.085536923187668  
```  
