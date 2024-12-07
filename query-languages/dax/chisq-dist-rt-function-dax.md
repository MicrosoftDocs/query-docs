---
description: "Learn more about: CHISQ.DIST.RT"
title: "CHISQ.DIST.RT function (DAX) | Microsoft Docs"
---
# CHISQ.DIST.RT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the right-tailed probability of the chi-squared distribution. 
  
The chi-squared distribution is associated with a chi-squared test. Use the chi-squared test to compare observed and expected values. For example, a genetic experiment might hypothesize that the next generation of plants will exhibit a certain set of colors. By comparing the observed results with the expected ones, you can decide whether your original hypothesis is valid.
  
## Syntax  
  
```dax
CHISQ.DIST.RT(<x>, <deg_freedom>)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`x`|The value at which you want to evaluate the distribution.|  
|`Deg_freedom`|The number of degrees of freedom.|
  
## Return value

The right-tailed probability of the chi-squared distribution.
  
## Remarks

- If x or deg_freedom is nonnumeric, an error is returned.

- If deg_freedom is not an integer, it is rounded.

- If x < 0, an error is returned.

- If deg_freedom < 1 or deg_freedom > 10^10, an error is returned.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example  
  
The following DAX query,
  
```dax
EVALUATE { CHISQ.DIST.RT(2, 5) }
```

Returns

|[Value] |
|---------|
|0.84914503608461    |
