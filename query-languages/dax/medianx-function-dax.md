---
title: "MEDIANX Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# MEDIANX Function (DAX)
  
Returns the median number of an expression evaluated for each row in a table.  
  
To return the median of numbers in a column, use [MEDIAN Function &#40;DAX&#41;](median-function-dax.md).  
  
## Syntax  
  
```  
MEDIANX(<table>, <expression>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return Value  
A decimal number.  
  
## Remarks  
The MEDIANX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the median, or an expression that evaluates to a column.  
  
Only the numbers in the column are counted. 

Logical values and text are ignored.

MEDIANX does not ignore blanks; however, MEDIAN does ignore blanks  
  
## Example  
The following computes the median age of customers who live in the USA.  
  
```  
=MEDIANX( FILTER(Customers, RELATED( Geography[Country]=”USA” ) ), Customers[Age] )  
```  
  
## See Also  
[MEDIAN Function &#40;DAX&#41;](median-function-dax.md)  
  
