---
description: "Learn more about: NORM.S.DIST"
title: "NORM.S.DIST function (DAX) | Microsoft Docs"
---
# NORM.S.DIST

Returns the standard normal distribution (has a mean of zero and a standard deviation of one).

## Syntax  
  
```dax
NORM.S.DIST(Z, Cumulative)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Z|The value for which you want the distribution.|  
|Cumulative|Cumulative is a logical value that determines the form of the function. If cumulative is TRUE, NORM.S.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.|
  
## Return value

The standard normal distribution (has a mean of zero and a standard deviation of one.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { NORM.S.DIST(1.333333, TRUE) }
```

Returns

|[Value]  |
|---------|
|0.908788725604095    |

## Related content  

[NORM.INV function](norm-inv-dax.md)  
[NORM.DIST function](norm-dist-dax.md)  
[NORM.S.INV](norm-s-inv-dax.md)  
