---
description: "Learn more about: NONFILTER"
title: "NONFILTER function (DAX) | Microsoft Docs"
ms.topic: reference
---
# NONFILTER

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Modifies how filters are applied while evaluating a GROUPCROSSAPPLY or GROUPCROSSAPPLYTABLE function.
  
## Syntax  
  
```dax
NONFILTER(<table expression>)
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table expression|Any table expression.|
  
## Return value

A table of values.  
  
## Remarks

- You use NONFILTER within the context GROUPCROSSAPPLY and GROUPCROSSAPPLYTABLE functions, to override the standard behavior of those functions.

- A NONFILTER makes the table expression permanently hidden from the filter context even if its columns may have lineage. Those columns with lineage act as if they are extension columns.

## Related content

- [Filter functions](filter-functions-dax.md)  
- [GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
- [GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
