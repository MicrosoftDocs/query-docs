---
description: "Learn more about: ALLSELECTEDAPPLY"
title: "ALLSELECTEDAPPLY function (DAX) | Microsoft Docs"
---
# ALLSELECTEDAPPLY

Modifies how filters are applied while evaluating a GROUPCROSSAPPLY or GROUPCROSSAPPLYTABLE function.
  
## Syntax  
  
```dax
ALLSELECTEDAPPLY(<table expression>)
```
  
### Parameters  
  
|Term|Definition|
|--------|--------------|
|table expression|Any table expression.|
  
## Return value

A table of values.
  
## Remarks

- You use ALLSELECTEDAPPLY within the context GROUPCROSSAPPLY and GROUPCROSSAPPLYTABLE functions, to override the standard behavior of those functions.

- When a filter is specified as ALLSELECTEDAPPLY, it is initially hidden in the filter context. Upon an ALLSELECTED inside CALCULATE or CALCULATETABLE, this table expression is enabled in fliter context.

## Related content

[Filter functions](filter-functions-dax.md)  
[GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
