---
title: "PERCENTILE.EXC Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PERCENTILE.EXC Function (DAX)

  
Returns the k-th percentile of values in a range, where k is in the range 0..1, exclusive.  
  
To return the percentile number of an expression evaluated for each row in a table, use [PERCENTILEX.EXC Function &#40;DAX&#41;](percentilex-exc-function-dax.md).  
  
## Syntax  
  
```  
PERCENTILE.EXC(<column>, <k>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A column containing the values that define relative standing.|  
|k|The percentile value in the range 0..1, exclusive.|  
  
## Return Value  
The k-th percentile of values in a range, where k is in the range 0..1, exclusive.  
  
## Remarks  
If column is empty, BLANK() is returned.  
  
If k is zero or blank, percentile rank of 1/(n+1) returns the smallest value. If zero, it is out of range and an error is returned.  
  
If k is nonnumeric or outside the range 0 to 1, an error is returned.  
  
If k is not a multiple of 1/(n + 1), PERCENTILE.EXC will interpolate to determine the value at the k-th percentile.  
  
PERCENTILE.EXC will interpolate when the value for the specified percentile is between two values in the array. If it cannot interpolate for the k percentile specified, an error is returned.  
  
## See Also  
[PERCENTILEX.EXC Function &#40;DAX&#41;](percentilex-exc-function-dax.md)  
  
