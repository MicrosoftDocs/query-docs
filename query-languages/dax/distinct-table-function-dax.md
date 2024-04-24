---
description: "Learn more about: DISTINCT (table)"
title: "DISTINCT (table) function (DAX) | Microsoft Docs"
---
# DISTINCT (table)

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a table by removing duplicate rows from another table or expression.
  
## Syntax  
  
```dax
DISTINCT(<table>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|The table from which unique rows are to be returned. The table can also be an expression that results in a table.|  
  
## Return value

A table containing only distinct rows.  
  
## Related functions

There is another version of the DISTINCT function, [DISTINCT (column)](distinct-function-dax.md), that takes a column name as input parameter.
  
## Example  

The following query:

```dax
EVALUATE DISTINCT( { (1, "A"), (2, "B"), (1, "A") } )
```

Returns table:

|[Value1]    |[Value2]  |
|---------|---------|
|1    |     A    |
|2    |     B    |

## Related content

[Filter functions](filter-functions-dax.md)  
[DISTINCT (column)](distinct-function-dax.md)  
[FILTER function](filter-function-dax.md)  
[RELATED function](related-function-dax.md)  
[VALUES function](values-function-dax.md)  
