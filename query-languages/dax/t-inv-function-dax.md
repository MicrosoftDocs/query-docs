---
description: "Learn more about: T.INV"
title: "T.INV function (DAX)"
---
# T.INV

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the left-tailed inverse of the Student's t-distribution.

## Syntax  
  
```dax
T.INV(Probability,Deg_freedom)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`Probability`|The probability associated with the Student's t-distribution.|  
|`Deg_freedom`|The number of degrees of freedom with which to characterize the distribution.|
  
## Return value

The left-tailed inverse of the Student's t-distribution.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { T.INV(0.75, 2) }
```

Returns

|[Value]  |
|---------|
|0.816496580927726   |

## Related content  

[T.INV.2T](t-inv-2t-function-dax.md)  
[T.DIST](t-dist-function-dax.md)  
[T.DIST.2T](t-dist-2t-function-dax.md)  
[T.DIST.RT](t-dist-rt-function-dax.md)  
