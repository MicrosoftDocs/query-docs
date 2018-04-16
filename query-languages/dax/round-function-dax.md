---
title: "ROUND Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ROUND Function (DAX)
Rounds a number to the specified number of digits.  
  
## Syntax  
  
```  
ROUND(<number>, <num_digits>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to round.|  
|**num_digits**|The number of digits to which you want to round. A negative value rounds digits to the left of the decimal point; a value of zero rounds to the nearest integer.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
If **num_digits** is greater than 0 (zero), then number is rounded to the specified number of decimal places.  
  
If **num_digits** is 0, the number is rounded to the nearest integer.  
  
If **num_digits** is less than 0, the number is rounded to the left of the decimal point.  
  
## Related Functions  
To always round up (away from zero), use the ROUNDUP function.  
  
To always round down (toward zero), use the ROUNDDOWN function.  
  
To round a number to a specific multiple (for example, to round to the nearest multiple of 0.5), use the MROUND function.  
  
You can use the functions TRUNC and INT to obtain the integer portion of the number.  
  
## Example  
The following formula rounds 2.15 up, to one decimal place. The expected result is 2.2.  
  
```  
=ROUND(2.15,1)  
```  
  
## Example  
The following formula rounds 21.5 to one decimal place to the left of the decimal point. The expected result is 20.  
  
```  
=ROUND(21.5,-1)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](mround-function-dax.md)  
[INT Function &#40;DAX&#41;](int-function-dax.md)  
[TRUNC Function &#40;DAX&#41;](trunc-function-dax.md)  
  
