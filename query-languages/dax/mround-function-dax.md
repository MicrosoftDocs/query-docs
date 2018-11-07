---
title: "MROUND Function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MROUND Function (DAX)
Returns a number rounded to the desired multiple.  
  
## Syntax  
  
```dax
MROUND(<number>, <multiple>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|The number to round.|  
|multiple|The multiple of significance to which you want to round the number.|  
  
## Return value  
A decimal number.  
  
## Remarks  
MROUND rounds up, away from zero, if the remainder of dividing **number** by the specified **multiple** is greater than or equal to half the value of **multiple**.  
  
## Example: Decimal Places  
  
### Description  
The following expression rounds 1.3 to the nearest multiple of .2. The expected result is 1.4.  
  
### Code  
  
```dax
=MROUND(1.3,0.2)  
```
  
## Example: Negative Numbers  
  
### Description  
The following expression rounds -10 to the nearest multiple of -3. The expected result is -9.  
  
### Code  
  
```dax
=MROUND(-10,-3)  
```
  
## Example: Error  
  
### Description  
The following expression returns an error, because the numbers have different signs.  
  
### Code  
  
```dax
=MROUND(5,-2)  
```
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](roundup-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](mround-function-dax.md)  
[INT Function &#40;DAX&#41;](int-function-dax.md)  
  
