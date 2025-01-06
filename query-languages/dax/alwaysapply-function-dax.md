---
description: "Learn more about: ALWAYSAPPLY"
title: "ALWAYSAPPLY function (DAX) | Microsoft Docs"
---
# ALWAYSAPPLY

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Modifies how filters are applied while evaluating a GROUPCROSSAPPLY or GROUPCROSSAPPLYTABLE function.
  
## Syntax
  
```dax
ALWAYSAPPLY(<table expression>)  
```
  
### Parameters
  
|Term|Definition|
|--------|--------------|
|table expression|Any table expression.|
  
## Return value

A table of values.
  
## Remarks

- You use ALWAYSAPPLY within the context GROUPCROSSAPPLY and GROUPCROSSAPPLYTABLE functions, to override the standard behavior of those functions.
  
- By default, a value filter does not affect measure if it doesn't change filter context. This behavior can be controlled by ALWAYSAPPLY function so that an empty table can still affect measure even if it doesn't change filter context.
  
## Related content

[Filter functions](filter-functions-dax.md)  
[GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
