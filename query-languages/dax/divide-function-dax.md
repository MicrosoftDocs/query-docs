---
description: "Learn more about: DIVIDE"
title: "DIVIDE function (DAX) | Microsoft Docs"
---
# DIVIDE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Performs division and returns alternate result or BLANK() on division by 0.  
  
## Syntax  
  
```dax
DIVIDE(<numerator>, <denominator> [,<alternateresult>])  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|numerator|The dividend or number to divide.|  
|denominator|The divisor or number to divide by.|  
|alternateresult|(Optional) The value returned when division by zero results in an error. When not provided, the default value is BLANK().|  
  
## Return value

- A decimal number.  
  
## Remarks

- Alternate result on divide by 0 must be a constant.  

- For best practices when using DIVIDE, see [DIVIDE function vs. divide operator (/) in DAX](best-practices/dax-divide-function-operator.md).
  
## Example

The following example returns 2.5.  
  
```dax
= DIVIDE(5,2)  
```
  
## Example 1

The following example returns BLANK.  
  
```dax
= DIVIDE(5,0)  
```
  
## Example 2

The following example returns 1.  
  
```dax
= DIVIDE(5,0,1)  
```
  
## Related content

[QUOTIENT function](quotient-function-dax.md)  
[Math and Trig functions](math-and-trig-functions-dax.md)  
