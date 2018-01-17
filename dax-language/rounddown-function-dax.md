---
title: "ROUNDDOWN Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.ROUNDDOWN.f1"
helpviewer_keywords: 
  - "ROUNDDOWN function"
  - "rounding"
ms.assetid: f188209b-0a0b-41b1-a769-01e9def2705e
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# ROUNDDOWN Function (DAX)
Rounds a number down, toward zero.  
  
## Syntax  
  
```  
ROUNDDOWN(<number>, <num_digits>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|A real number that you want rounded down.|  
|**num_digits**|The number of digits to which you want to round. Negative rounds to the left of the decimal point; zero to the nearest integer.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
If **num_digits** is greater than 0 (zero), then the value in **number** is rounded down to the specified number of decimal places.  
  
If **num_digits** is 0, then the value in **number** is rounded down to the nearest integer.  
  
If **num_digits** is less than 0, then the value in **number** is rounded down to the left of the decimal point.  
  
## Related Functions  
ROUNDDOWN behaves like ROUND, except that it always rounds a number down. The INT function also rounds down, but with INT the result is always an integer, whereas with ROUNDDOWN you can control the precision of the result.  
  
## Example  
The following example rounds 3.14159 down to three decimal places. The expected result is 3.141.  
  
```  
=ROUNDDOWN(3.14159,3)  
```  
  
## Example  
The following example rounds the value of 31415.92654 down to 2 decimal places to the left of the decimal. The expected result is 31400.  
  
```  
=ROUNDDOWN(31415.92654, -2)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](../DAX/math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](../DAX/round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](../DAX/roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](../DAX/rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](../DAX/mround-function-dax.md)  
[INT Function &#40;DAX&#41;](../DAX/int-function-dax.md)  
  
