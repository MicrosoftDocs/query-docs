---
description: "Learn more about: NORM.INV"
title: "NORM.INV function (DAX) | Microsoft Docs"
---
# NORM.INV

The inverse of the normal cumulative distribution for the specified mean and standard deviation.
 
  
## Syntax  
  
```dax
NORM.INV(Probability, Mean, Standard_dev)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability corresponding to the normal distribution.|  
|Mean|The arithmetic mean of the distribution.|
|Standard_dev|The standard deviation of the distribution.|
  
## Return value

Returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
```dax
EVALUATE { NORM.INV(0.908789, 40, 1.5) }
```

Returns

|[Value]  |
|---------|
|42.00000200956628780274132    |

## Related content  

[NORM.S.INV](norm-s-inv-dax.md)   
[NORM.S.DIST function](norm-s-dist-dax.md)   
[NORM.DIST function](norm-dist-dax.md)   
