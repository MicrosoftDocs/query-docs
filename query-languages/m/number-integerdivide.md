---
title: "Number.IntegerDivide | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.IntegerDivide

  
## About  
Divides two numbers and returns the whole part of the resulting number.  
  
## Syntax

<pre>
Number.IntegerDivide (number1 as nullable number,  number2 as nullable number,  optional precision as nullable number) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|number1|The Dividend.|  
|number2|The Divisor.|  
|optional precision|Precision of the result.|  
  
## Example  
  
```powerquery-m
Number.IntegerDivide(9.2, 3.1) equals 2  
```  
