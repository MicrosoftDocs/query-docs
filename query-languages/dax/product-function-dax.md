---
title: "PRODUCT function (DAX) | Microsoft Docs"
ms.service: powerbi 

ms.date: 11/07/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# PRODUCT function (DAX)
  
Returns the product of the numbers in a column.  
  
To return the product of an expression evaluated for each row in a table, use [PRODUCTX function &#40;DAX&#41;](productx-function-dax.md).  
  
## Syntax  
  
```dax
PRODUCT(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|column|The column that contains the numbers for which the product is to be computed.|  
  
## Return value  
A decimal number.  
  
## Remarks  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
PRODUCT( Table[Column] ) is equivalent to PRODUCTX( Table, Table[Column] )  
  
## Example  
The following computes the product of the AdjustedRates column in an Annuity table:  
  
```dax
=PRODUCT( Annuity[AdjustedRates] )  
```
  
## See also  
[PRODUCTX function &#40;DAX&#41;](productx-function-dax.md)  
  
