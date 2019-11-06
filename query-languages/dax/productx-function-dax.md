---
title: "PRODUCTX function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 12/10/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# PRODUCTX

Returns the product of an expression evaluated for each row in a table.  
  
To return the product of the numbers in a column, use [PRODUCT function &#40;DAX&#41;](product-function-dax.md).  
  
## Syntax  
  
```dax
PRODUCTX(<table>, <expression>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value  
A decimal number.  
  
## Remarks  
The PRODUCTX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the product, or an expression that evaluates to a column.  
  
Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  
  
## Example  
The following computes the future value of an investment:  
  
```dax
= [PresentValue] * PRODUCTX( AnnuityPeriods, 1+[FixedInterestRate] )  
```
  
## See also  
[PRODUCT function &#40;DAX&#41;](product-function-dax.md)  
  
