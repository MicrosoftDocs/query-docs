---
description: "Learn more about: CHISQ.INV.RT"
title: "CHISQ.INV.RT function (DAX) | Microsoft Docs"
---
# CHISQ.INV.RT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the inverse of the right-tailed probability of the chi-squared distribution.  
  
If probability = CHISQ.DIST.RT(x,...), then CHISQ.INV.RT(probability,...) = x. Use this function to compare observed results with expected ones in order to decide whether your original hypothesis is valid.  
  
## Syntax  
  
```dax
CHISQ.INV.RT(probability,deg_freedom)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|Probability|A probability associated with the chi-squared distribution.|  
|Deg_freedom|The number of degrees of freedom.|  
  
## Return value

Returns the inverse of the right-tailed probability of the chi-squared distribution.  
  
## Remarks

- If either argument is nonnumeric, CHISQ.INV.RT returns the #VALUE! error value.  
  
- If probability &lt; 0 or probability &gt; 1, CHISQ.INV.RT returns the #NUM! error value.  
  
- If deg_freedom is not an integer, it is rounded.  
  
- If deg_freedom &lt; 1, CHISQ.INV.RT returns the #NUM! error value.  
  
- Given a value for probability, CHISQ.INV.RT seeks that value x such that CHISQ.DIST.RT(x, deg_freedom) = probability. Thus, precision of CHISQ.INV.RT depends on precision of CHISQ.DIST.RT. CHISQ.INV.RT uses an iterative search technique. If the search has not converged after 64 iterations, the function returns the #N/A error value.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]
