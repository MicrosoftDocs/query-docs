---
description: "Learn more about: SINH"
title: "SINH function (DAX) | Microsoft Docs"
---
# SINH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the hyperbolic sine of a number.  
  
## Syntax  
  
```dax
SINH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Required. Any real number.|  
  
## Return value

Returns the hyperbolic sine of a number.  
  
## Remarks

- The formula for the hyperbolic sine is:  

    $$\text{SINH}(z) = \frac{e^{z} - e^{-z}}{2}$$

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example  

Probability of obtaining a result of less than 1.03 seconds.

```dax
= 2.868*SINH(0.0342\*1.03)
```

Returns, 0.1010491
