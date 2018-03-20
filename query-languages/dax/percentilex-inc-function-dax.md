---
title: "PERCENTILEX.INC Function (DAX) | Microsoft Docs"
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
ms.assetid: 2c8a98f8-6121-477c-a828-0ec5845b49bf
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# PERCENTILEX.INC Function (DAX)
  
Returns the percentile number of an expression evaluated for each row in a table.  
  
To return the percentile of numbers in a column, use [PERCENTILE.INC Function &#40;DAX&#41;](percentile-inc-function-dax.md).  
  
## Syntax  
  
```  
PERCENTILEX.INC(<table>, <expression>;, k)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
|k|The desired percentile value in the range 0 to 1 inclusive.|  
  
## Return Value  
The percentile number of an expression evaluated for each row in a table.  
  
## Remarks  
If k is zero or blank, percentile rank of 1/(n - 1) returns the smallest value. If zero, it is out of range and an error is returned.  
  
If k is nonnumeric or outside the range 0 to 1, an error is returned.  
  
If k is not a multiple of 1/(n - 1), PERCENTILEX.EXC will interpolate to determine the value at the k-th percentile.  
  
PERCENTILEX.INC will interpolate when the value for the specified percentile is between two values in the array. If it cannot interpolate for the k percentile specified, an error is returned.  
  
## See Also  
[PERCENTILE.INC Function &#40;DAX&#41;](percentile-inc-function-dax.md)  
  
