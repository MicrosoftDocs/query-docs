---
description: "Learn more about: T.DIST"
title: "T.DIST function (DAX) | Microsoft Docs"
---
# T.DIST

Returns the Student's left-tailed t-distribution.
  
## Syntax  
  
```dax
T.DIST(X,Deg_freedom,Cumulative)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|X|The numeric value at which to evaluate the distribution.|  
|Deg_freedom |An integer indicating the number of degrees of freedom.|
|Cumulative|A logical value that determines the form of the function. If cumulative is TRUE, T.DIST returns the cumulative distribution function; if FALSE, it returns the probability density function.|
  
## Return value

The Student's left-tailed t-distribution.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { T.DIST(60, 1, TRUE) }
```

Returns,

|[Value]  |
|---------|
|0.994695326367377     |

## Related content  

[T.DIST.2T](t-dist-2t-dax.md)  
[T.DIST.RT](t-dist-rt-dax.md)  
[T.INV](t-inv-dax.md)  
[T.INV.2t](t-inv-2t-dax.md)  
  
