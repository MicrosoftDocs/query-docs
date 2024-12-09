---
description: "Learn more about: T.DIST.2T"
title: "T.DIST.2T function (DAX)"
---
# T.DIST.2T

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the two-tailed Student's t-distribution.
  
## Syntax  
  
```dax
T.DIST.2T(X,Deg_freedom)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`X`|The numeric value at which to evaluate the distribution.|  
|`Deg_freedom` |An integer indicating the number of degrees of freedom.|
  
## Return value

The two-tailed Student's t-distribution.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { T.DIST.2T(1.959999998, 60) }
```

Returns

|[Value]  |
|---------|
|0.054644929975921     |

## Related content  

[T.DIST](t-dist-function-dax.md)  
[T.DIST.RT](t-dist-rt-function-dax.md)  
[T.INV](t-inv-function-dax.md)  
[T.INV.2t](t-inv-2t-function-dax.md)  
  
