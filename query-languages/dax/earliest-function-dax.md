---
description: "Learn more about: EARLIEST"
title: "EARLIEST function (DAX)"
---
# EARLIEST

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Returns the current value of the specified column in an outer evaluation pass of the specified column.  
  
## Syntax  
  
```dax
EARLIEST(<column>)  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|`column`|A reference to a column.|  
  
## Return value

A column with filters removed.  
  
## Remarks

- The EARLIEST function is similar to EARLIER, but lets you specify one additional level of recursion.  

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The current sample data does not support this scenario.  
  
```dax
= EARLIEST(<column>)  
```
  
## Related content

[EARLIER function](earlier-function-dax.md)  
[Filter functions](filter-functions-dax.md)  
