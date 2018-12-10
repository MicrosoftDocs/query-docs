---
title: "MEDIAN function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MEDIAN
  
Returns the median of numbers in a column.  
  
To return the median of an expresssion evaluated for each row in a table, use [MEDIANX function &#40;DAX&#41;](medianx-function-dax.md).  
  
## Syntax  
  
```dax
MEDIAN(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers for which the median is to be computed.|  
  
## Return value  
A decimal number.  
  
## Remarks  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
MEDIAN( Table[Column] ) is equivalent to MEDIANX( Table, Table[Column] ).  
  
## Example  
The following computes the median of a column named Age in a table named Customers:  
  
```dax
=MEDIAN( Customers[Age] )  
```
  
## See also  
[MEDIANX function &#40;DAX&#41;](medianx-function-dax.md)  
  
