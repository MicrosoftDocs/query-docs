---
title: "Number.Mod | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Mod

  
## About  
Divides two numbers and returns the remainder of the resulting number.  
  
## Syntax

<pre>
Number.Mod(number as nullable number, divisor as nullable number, optional precision as nullable number) as nullable number 
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number|Dividend or numerator.|  
|divisor|Divisor or denominator.|  
  
## Example  
  
```powerquery-m
Number.Mod(83, 9) equals 2  
```  
