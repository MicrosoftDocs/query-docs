---
title: "GEOMEAN function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# GEOMEAN function (DAX)
  
Returns the geometric mean of the numbers in a column.  
  
To return the geometric mean of an expression evaluated for each row in a table, use [GEOMEANX function &#40;DAX&#41;](geomeanx-function-dax.md).  
  
## Syntax  
  
```dax
GEOMEAN(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers for which the geometric mean is to be computed.|  
  
## Return value  
A decimal number.  
  
## Remarks  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
GEOMEAN( Table[Column] ) is equivalent to GEOMEANX( Table, Table[Column] )  
  
## Example  
The following computes the geometric mean of the Return column in the Investment table:  
  
```dax
=GEOMEAN( Investment[Return] )  
```
  
## See also  
[GEOMEANX function &#40;DAX&#41;](geomeanx-function-dax.md)  
  
