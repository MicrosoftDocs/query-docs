---
description: "Learn more about: ALLSELECTEDREMOVE"
title: "ALLSELECTEDREMOVE function (DAX) | Microsoft Docs"
---
# ALLSELECTEDREMOVE

Modifies how filters are applied while evaluating a GROUPCROSSAPPLY or GROUPCROSSAPPLYTABLE function.
  
## Syntax  
  
```dax
ALLSELECTEDREMOVE(<table expression>[, <column>[, <column>[,…]]])
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table expression|Any table expression.|  
|column|Column in the table expression.|
  
## Return value

A table of values.  
  
## Remarks

- You use ALLSELECTEDREMOVE within the context GROUPCROSSAPPLY and GROUPCROSSAPPLYTABLE functions, to override the standard behavior of those functions.

- When doing ALLSELECTED on a column that appears on the list of ALLSELECTEDREMOVE column parameter, then this column from this table expression will not participate in the filter context. The same column from other table expression in the filter context is not changed.

- It is possible to specify a subset of columns of the table expression. When no column is supplied, then it's equivalent to supplying all columns of the table expression to ALLSELECTEDREMOVE

## Related content

[Filter functions](filter-functions-dax.md)  
[GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
