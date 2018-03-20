---
title: "PERCENTILE.INC Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: ca18a3b0-5a36-45a3-a279-1d33e359daf2
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# PERCENTILE.INC Function (DAX)

  
Returns the k-th percentile of values in a range, where k is in the range 0..1, inclusive.  
  
To return the percentile number of an expression evaluated for each row in a table, use [PERCENTILEX.INC Function &#40;DAX&#41;](percentilex-inc-function-dax.md).  
  
## Syntax  
  
```  
PERCENTILE.INC(<column>, <k>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|A column containing the values that define relative standing.|  
|k|The percentile value in the range 0..1, inclusive.|  
  
## Return Value  
The k-th percentile of values in a range, where k is in the range 0..1, inclusive.  
  
## Remarks  
If column is empty, BLANK() is returned.  
  
If k is zero or blank, percentile rank of 1/(n+1) returns the smallest value. If zero, it is out of range and an error is returned.  
  
If k is nonnumeric or outside the range 0 to 1, an error is returned.  
  
If k is not a multiple of 1/(n + 1), PERCENTILE.INC will interpolate to determine the value at the k-th percentile.  
  
PERCENTILE.INC will interpolate when the value for the specified percentile is between two values in the array. If it cannot interpolate for the k percentile specified, an error is returned.  
  
## See Also  
[PERCENTILEX.INC Function &#40;DAX&#41;](percentilex-inc-function-dax.md)  
  
