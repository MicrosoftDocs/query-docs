---
title: "MINA Function (DAX) | Microsoft Docs"
ms.prod: dax
ms.date: 5/22/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MINA Function (DAX)
Returns the smallest value in a column, including any logical values and numbers represented as text.  
  
## Syntax  
  
```dax
MINA(<column>)  
```
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**column**|The column for which you want to find the minimum value.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The MINA function takes as argument a column that contains numbers, and determines the smallest value as follows:  
  
-   If the column contains no numeric values, MINA returns 0 (zero).  
  
-   Rows in the column that evaluates to logical values, such as TRUE and FALSE are treated as 1 if TRUE and 0 (zero) if FALSE.  
  
-   Empty cells are ignored.  
  
If you do not want to include logical values and text as part of the calculation, use the MIN function instead.  
  
## Example  
The following expression returns the minimum freight charge from the table, InternetSales.  
  
```dax
=MINA(InternetSales[Freight])  
```
  
## Example  
The following expression returns the minimum value in the column, PostalCode. Because the data type of the column is text, the function does not find any numeric values, and the formula returns zero (0).  
  
```dax
=MINA([PostalCode])  
```
  
## See Also  
[MIN Function &#40;DAX&#41;](min-function-dax.md)  
[MINA Function &#40;DAX&#41;](mina-function-dax.md)  
[MINX Function &#40;DAX&#41;](minx-function-dax.md)  
[Statistical Functions &#40;DAX&#41;](statistical-functions-dax.md)  
  
