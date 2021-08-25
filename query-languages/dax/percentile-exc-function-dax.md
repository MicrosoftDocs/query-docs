---
description: "Learn more about: PERCENTILE.EXC"
title: "PERCENTILE.EXC function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/10/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# PERCENTILE.EXC
  
Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive.  
  
To return the percentile number of an expression evaluated for each row in a table, use [PERCENTILEX.EXC function](percentilex-exc-function-dax.md).  
  
## Syntax  
  
```dax
PERCENTILE.EXC(<column>, <k>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A column containing the values that define relative standing.|  
|k|The percentile value in the range 0..1, exclusive.|  
  
## Return value

The k-th percentile of values in a range, where k is in the range 0..1, exclusive.  
  
## Remarks

- If column is empty, BLANK() is returned.  
  
- If k is zero or blank, percentile rank of 1/(n+1) returns the smallest value. If zero, it is out of range and an error is returned.  
  
- If k is nonnumeric or outside the range 0 to 1, an error is returned.  
  
- If k is not a multiple of 1/(n + 1), PERCENTILE.EXC will interpolate to determine the value at the k-th percentile.  
  
- PERCENTILE.EXC will interpolate when the value for the specified percentile is between two values in the array. If it cannot interpolate for the k percentile specified, an error is returned.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## See also

[PERCENTILEX.EXC](percentilex-exc-function-dax.md)  
