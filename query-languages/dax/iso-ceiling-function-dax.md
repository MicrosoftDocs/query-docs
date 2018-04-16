---
title: "ISO.CEILING Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# ISO.CEILING Function (DAX)
Rounds a number up, to the nearest integer or to the nearest multiple of significance.  
  
## Syntax  
  
```  
ISO.CEILING(<number>[, <significance>])  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**number**|The number you want to round, or a reference to a column that contains numbers.|  
|**significance**|(optional) The multiple of significance to which you want to round. For example, to round to the nearest integer, type 1. If the unit of significance is not specified, the number is rounded up to the nearest integer.|  
  
## Return Value  
A number, of the same type as the *number* argument, rounded as specified.  
  
## Remarks  
There are two CEILING functions in DAX, with the following differences:  
  
-   The CEILING function emulates the behavior of the CEILING function in Excel.  
  
-   The ISO.CEILING function follows the ISO-defined behavior for determining the ceiling value.  
  
The two functions return the same value for positive numbers, but different values for negative numbers. When using a positive multiple of significance, both CEILING and ISO.CEILING round negative numbers upward (toward positive infinity). When using a negative multiple of significance, CEILING rounds negative numbers downward (toward negative infinity), while ISO.CEILING rounds negative numbers upward (toward positive infinity).  
  
The result type is usually the same type of the significance used as argument with the following exceptions:  
  
-   If the first argument is of currency type then the result will be currency type.  
  
-   If the optional argument is not included the result is of integer type.  
  
-   If the significance argument is of Boolean type then the result is of integer type.  
  
-   If the significance argument is non-numeric type then the result is of real type.  
  
## Example: Positive Numbers  
  
### Description  
The following formula returns 4.45. This might be useful if you want to avoid using smaller units in your pricing. If an existing product is priced at $4.42, you can use ISO.CEILING to round prices up to the nearest unit of five cents.  
  
### Code  
  
```  
=ISO.CEILING(4.42,0.05)  
```  
  
## Example: Negative Numbers  
  
### Description  
The following formula returns the ISO ceiling value of -4.40.  
  
### Code  
  
```  
=ISO.CEILING(-4.42,0.05)  
```  
  
## See Also  
[Math and Trig Functions &#40;DAX&#41;](math-and-trig-functions-dax.md)  
[FLOOR Function &#40;DAX&#41;](floor-function-dax.md)  
[CEILING Function &#40;DAX&#41;](ceiling-function-dax.md)  
[ROUNDUP Function &#40;DAX&#41;](roundup-function-dax.md)  
  
