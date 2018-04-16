---
title: "ROUNDUP Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ROUNDUP Function (DAX)
Rounds a number up, away from 0 (zero).  
  
## Syntax  
  
```  
ROUNDUP(<number>, <num_digits>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|A real number that you want to round up.|  
|**num_digits**|The number of digits to which you want to round. A negative value for **num_digits** rounds to the left of the decimal point; if **num_digits** is zero or is omitted, **number** is rounded to the nearest integer.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
ROUNDUP behaves like ROUND, except that it always rounds a number up.  
  
-   If **num_digits** is greater than 0 (zero), then the number is rounded up to the specified number of decimal places.  
  
-   If **num_digits** is 0, then number is rounded up to the nearest integer.  
  
-   If **num_digits** is less than 0, then number is rounded up to the left of the decimal point.  
  
## Related Functions  
ROUNDUP behaves like ROUND, except that it always rounds a number up.  
  
## Example  
The following formula rounds Pi to four decimal places. The expected result is 3.1416.  
  
```  
=ROUNDUP(PI(),4)  
```  
  
## Example: Decimals as Second Argument  
  
### Description  
The following formula rounds 1.3 to the nearest multiple of 0.2. The expected result is 2.  
  
### Code  
  
```  
=ROUNDUP(1.3,0.2)  
```  
  
## Example: Negative Number as Second Argument  
  
### Description  
The following formula rounds the value in the column, **FreightCost**, with the expected results shown in the following table:  
  
### Code  
  
```  
=ROUNDUP([Values],-1)  
```  
  
### Comments  
When **num_digits** is less than zero, the number of places to the left of the decimal sign is increased by the value you specify.  
  
|FreightCost|Expected Result|  
|---------------|-------------------|  
|13.25|20|  
|2.45|10|  
|25.56|30|  
|1.34|10|  
|345.01|350|  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[ROUND Function &#40;DAX&#41;](round-function-dax.md)  
[ROUNDDOWN Function &#40;DAX&#41;](rounddown-function-dax.md)  
[MROUND Function &#40;DAX&#41;](mround-function-dax.md)  
[INT Function &#40;DAX&#41;](int-function-dax.md)  
  
