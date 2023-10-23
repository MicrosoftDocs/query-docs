---
description: "Learn more about: MEDIANX"
title: "MEDIANX function (DAX) | Microsoft Docs"
---
# MEDIANX
  
Returns the median number of an expression evaluated for each row in a table.  
  
To return the median of numbers in a column, use [MEDIAN function](median-function-dax.md).  
  
## Syntax  
  
```dax
MEDIANX(<table>, <expression>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value

A decimal number.  
  
## Remarks

- The MEDIANX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the median, or an expression that evaluates to a column.  
  
- Only the numbers in the column are counted. 

- Logical values and text are ignored.

- MEDIANX does not ignore blanks; however, MEDIAN does ignore blanks  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following computes the median age of customers who live in the USA.  
  
```dax
= MEDIANX( FILTER(Customers, RELATED( Geography[Country]="USA" ) ), Customers[Age] )  
```
  
## See also

[MEDIAN function](median-function-dax.md)  
