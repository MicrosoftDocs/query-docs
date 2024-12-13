---
description: "Learn more about: ISCROSSFILTERED"
title: "ISCROSSFILTERED function (DAX)"
---
# ISCROSSFILTERED

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns `TRUE` when the specified table or column is cross-filtered.
  
## Syntax  
  
```dax
ISCROSSFILTERED(<TableNameOrColumnName>)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|`TableNameOrColumnName`|The name of an existing table or column. It cannot be an expression.|
  
## Return value

``TRUE`` when `ColumnName` or a column of `TableName` is being cross-filtered. Otherwise returns `FALSE`.
  
## Remarks  
  
- A column or table is said to be cross-filtered when a filter is applied to `ColumnName`, any column of `TableName`, or to any column of a related table.

- A column or table is said to be filtered directly when a filter is applied to `ColumnName` or to any column of `TableName`. Therefore, the [ISFILTERED](isfiltered-function-dax.md) function also returns `TRUE` when `ColumnName` or any column of `TableName` is filtered.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Related content

[ISFILTERED function](isfiltered-function-dax.md)  
[FILTERS function](filters-function-dax.md)  
[HASONEFILTER function](hasonefilter-function-dax.md)  
[HASONEVALUE function](hasonevalue-function-dax.md)  
