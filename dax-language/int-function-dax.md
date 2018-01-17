---
title: "INT Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.INT.f1"
helpviewer_keywords: 
  - "INT function"
  - "integers"
ms.assetid: 31c50282-9a07-495d-99a3-11d62c1a6916
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# INT Function (DAX)
Rounds a number down to the nearest integer.  
  
## Syntax  
  
```  
INT(<number>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to round down to an integer|  
  
## Return Value  
A whole number.  
  
## Remarks  
TRUNC and INT are similar in that both return integers. TRUNC removes the fractional part of the number. INT rounds numbers down to the nearest integer based on the value of the fractional part of the number. INT and TRUNC are different only when using negative numbers: `TRUNC(-4.3)` returns -4, but `INT(-4.3)` returns -5 because -5 is the lower number.  
  
## Example  
The following expression rounds the value to 1. If you use the ROUND function, the result would be 2.  
  
```  
=INT(1.5)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](../DAX/round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](../DAX/roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](../DAX/rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](../DAX/mround-function-dax.md)  
  
