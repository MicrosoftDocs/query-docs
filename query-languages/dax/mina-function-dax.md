---
description: "Learn more about: MINA"
title: "MINA function (DAX)"
---
# MINA

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the smallest value in a column.
  
## Syntax  
  
```dax
MINA(<column>)  
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|`column`|The column for which you want to find the minimum value.|  
  
## Return value

The smallest value.  
  
## Remarks

- The MINA function takes as argument a column that contains numbers, and determines the smallest value as follows:  
  - If the column contains no values, MINA returns 0 (zero).  
  - Rows in the column that evaluates to logical values, such as `TRUE` and `FALSE` are treated as 1 if `TRUE` and 0 (zero) if `FALSE`.
  - Empty cells are ignored.  
  
- If you want to compare text values, use the MIN function.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example 1

The following expression returns the minimum freight charge from the table, InternetSales.  
  
```dax
= MINA(InternetSales[Freight])  
```
  
## Example 2

The following expression returns the minimum value in the column, PostalCode. Because the data type of the column is text, the function does not find any values, and the formula returns zero (0).  
  
```dax
= MINA([PostalCode])  
```
  
## Related content

[MIN function](min-function-dax.md)  
[MINX function](minx-function-dax.md)  
[Statistical functions](statistical-functions-dax.md)  
