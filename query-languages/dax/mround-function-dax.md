---
description: "Learn more about: MROUND"
title: "MROUND function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# MROUND

Returns a number rounded to the desired multiple.  
  
## Syntax  
  
```dax
MROUND(<number>, <multiple>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number to round.|  
|multiple|The multiple of significance to which you want to round the number.|  
  
## Return value

A decimal number.  
  
## Remarks

MROUND rounds up, away from zero, if the remainder of dividing **number** by the specified **multiple** is greater than or equal to half the value of **multiple**.  
  
## Example: Decimal Places  

The following expression rounds 1.3 to the nearest multiple of .2. The expected result is 1.4.  
  
```dax
= MROUND(1.3,0.2)  
```
  
## Example: Negative Numbers  
  
The following expression rounds -10 to the nearest multiple of -3. The expected result is -9.  
  
```dax
= MROUND(-10,-3)  
```
  
## Example: Error  

The following expression returns an error, because the numbers have different signs.
  
```dax
= MROUND(5,-2)  
```
  
## See also

[Math and Trig functions](math-and-trig-functions-dax.md)  
[ROUND function](round-function-dax.md)  
[ROUNDUP function](roundup-function-dax.md)  
[ROUNDDOWN function](rounddown-function-dax.md)  
[MROUND function](mround-function-dax.md)  
[INT function](int-function-dax.md)  
