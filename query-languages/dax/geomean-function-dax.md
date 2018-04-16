---
title: "GEOMEAN Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# GEOMEAN Function (DAX)
  
Returns the geometric mean of the numbers in a column.  
  
To return the geometric mean of an expression evaluated for each row in a table, use [GEOMEANX Function &#40;DAX&#41;](geomeanx-function-dax.md).  
  
## Syntax  
  
```  
GEOMEAN(<column>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers for which the geometric mean is to be computed.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
GEOMEAN( Table[Column] ) is equivalent to GEOMEANX( Table, Table[Column] )  
  
## Example  
The following computes the geometric mean of the Return column in the Investment table:  
  
```  
=GEOMEAN( Investment[Return] )  
```  
  
## See Also  
[GEOMEANX Function &#40;DAX&#41;](geomeanx-function-dax.md)  
  
