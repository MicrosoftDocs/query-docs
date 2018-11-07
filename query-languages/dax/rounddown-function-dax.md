---
title: "ROUNDDOWN Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ROUNDDOWN Function (DAX)
Rounds a number down, toward zero.  
  
## Syntax  
  
```dax
ROUNDDOWN(<number>, <num_digits>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|A real number that you want rounded down.|  
|num_digits|The number of digits to which you want to round. Negative rounds to the left of the decimal point; zero to the nearest integer.|  
  
## Return value  
A decimal number.  
  
## Remarks  
If **num_digits** is greater than 0 (zero), then the value in **number** is rounded down to the specified number of decimal places.  
  
If **num_digits** is 0, then the value in **number** is rounded down to the nearest integer.  
  
If **num_digits** is less than 0, then the value in **number** is rounded down to the left of the decimal point.  
  
## Related Functions  
ROUNDDOWN behaves like ROUND, except that it always rounds a number down. The INT function also rounds down, but with INT the result is always an integer, whereas with ROUNDDOWN you can control the precision of the result.  
  
## Example  
The following example rounds 3.14159 down to three decimal places. The expected result is 3.141.  
  
```dax
=ROUNDDOWN(3.14159,3)  
```
  
## Example  
The following example rounds the value of 31415.92654 down to 2 decimal places to the left of the decimal. The expected result is 31400.  
  
```dax
=ROUNDDOWN(31415.92654, -2)  
```
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](mround-function-dax.md)  
[INT Function &#40;DAX&#41;](int-function-dax.md)  
  
