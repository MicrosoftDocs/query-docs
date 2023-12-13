---
description: "Learn more about: ATANH"
title: "ATANH function (DAX) | Microsoft Docs"
---
# ATANH

Returns the inverse hyperbolic tangent of a number. Number must be between -1 and 1 (excluding -1 and 1). The inverse hyperbolic tangent is the value whose hyperbolic tangent is *number*, so ATANH(TANH(number)) equals *number*.  
  
## Syntax  
  
```dax
ATANH(number)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|number|Any real number between 1 and -1.|  
  
## Return value

Returns the inverse hyperbolic tangent of a number.  

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|= ATANH(0.76159416)|Inverse hyperbolic tangent of 0.76159416|1.00000001|  
|= ATANH(-0.1)||-0.100335348|  
||||  

## Related content

[ATAN function](atan-function-dax.md)  
