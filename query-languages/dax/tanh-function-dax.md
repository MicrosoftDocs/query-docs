---
description: "Learn more about: TANH"
title: "TANH function (DAX) | Microsoft Docs"
---
# TANH

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the hyperbolic tangent of a number.  
  
## Syntax  
  
```dax
TANH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`number`|Required. Any real number.|  
  
## Return value

Returns the hyperbolic tangent of a number.  
  
## Remarks

- The formula for the hyperbolic tangent is:  

    $$\text{TANH}(z) = \frac{\text{SINH}(z)}{\text{COSH}(z)}$$

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|`= TANH(-2)`|Hyperbolic tangent of -2 (-0.96403)|-0.964028|  
|`= TANH(0)`|Hyperbolic tangent of 0 (0)|0|  
|`= TANH(0.5)`|Hyperbolic tangent of 0.5 (0.462117)|0.462117|  
