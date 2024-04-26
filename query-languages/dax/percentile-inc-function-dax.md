---
description: "Learn more about: PERCENTILE.INC"
title: "PERCENTILE.INC function (DAX) | Microsoft Docs"
---
# PERCENTILE.INC

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
  
Returns the k-th percentile of values in a range, where k is in the range 0..1, inclusive.  
  
To return the percentile number of an expression evaluated for each row in a table, use [PERCENTILEX.INC](percentilex-inc-function-dax.md).  
  
## Syntax  
  
```dax
PERCENTILE.INC(<column>, <k>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A column containing the values that define relative standing.|  
|k|The percentile value in the range 0..1, inclusive.|  
  
## Return value

The k-th percentile of values in a range, where k is in the range 0..1, inclusive.  
  
## Remarks

- If column is empty, BLANK() is returned.  
  
- If k is zero or blank, percentile rank of 1/(n+1) returns the smallest value. If zero, it is out of range and an error is returned.  
  
- If k is nonnumeric or outside the range 0 to 1, an error is returned.  
  
- If k is not a multiple of 1/(n + 1), PERCENTILE.INC will interpolate to determine the value at the k-th percentile.  
  
- PERCENTILE.INC will interpolate when the value for the specified percentile is between two values in the array. If it cannot interpolate for the k percentile specified, an error is returned.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Related content

[PERCENTILEX.INC](percentilex-inc-function-dax.md)  
