---
description: "Learn more about: GEOMEANX"
title: "GEOMEANX function (DAX) | Microsoft Docs"
---
# GEOMEANX

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]
  
Returns the geometric mean of an expression evaluated for each row in a table.  
  
To return the geometric mean of the numbers in a column, use [GEOMEAN function](geomean-function-dax.md).  
  
## Syntax  
  
```dax
GEOMEANX(<table>, <expression>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table containing the rows for which the expression will be evaluated.|  
|expression|The expression to be evaluated for each row of the table.|  
  
## Return value

A decimal number.  
  
## Remarks

- The GEOMEANX function takes as its first argument a table, or an expression that returns a table. The second argument is a column that contains the numbers for which you want to compute the geometric mean, or an expression that evaluates to a column.  
  
- Only the numbers in the column are counted. Blanks, logical values, and text are ignored.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following computes the geometric mean of the ReturnPct column in the Investments table:  
  
```dax
= GEOMEANX( Investments, Investments[ReturnPct] + 1 )  
```
  
## Related content

[GEOMEAN function](geomean-function-dax.md)  
