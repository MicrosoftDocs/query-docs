---
description: "Learn more about: T.DIST.RT"
title: "T.DIST.RT function (DAX) | Microsoft Docs"
---
# T.DIST.RT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the right-tailed Student's t-distribution.

## Syntax  
  
```dax
T.DIST.RT(X,Deg_freedom)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`X`|The numeric value at which to evaluate the distribution.|  
|`Deg_freedom` |An integer indicating the number of degrees of freedom.|
  
## Return value

The right-tailed Student's t-distribution.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { T.DIST.RT(1.959999998, 60) }
```

Returns

|[Value]  |
|---------|
|0.0273224649879605     |

## Related content  

[T.DIST](t-dist-function-dax.md)  
[T.DIST.2T](t-dist-2t-function-dax.md)  
[T.INV](t-inv-function-dax.md)  
[T.INV.2t](t-inv-2t-function-dax.md)  
