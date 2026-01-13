---
description: "Learn more about: SHADOWCLUSTER"
title: "SHADOWCLUSTER function (DAX) | Microsoft Docs"
ms.topic: reference
---
# SHADOWCLUSTER

[!INCLUDE[applies-to-measures-columns-tables](includes/applies-to-measures-columns-tables.md)]

Modifies how filters are applied while evaluating a GROUPCROSSAPPLY or GROUPCROSSAPPLYTABLE function.
  
## Syntax  
  
```dax
SHADOWCLUSTER(<table expression>)
```
  
### Parameters  
  
|Term|Definition|
|--------|--------------|
|table expression|Any table expression.|
  
## Return value

A table of values.
  
## Remarks

- You use SHADOWCLUSTER within the context GROUPCROSSAPPLY and GROUPCROSSAPPLYTABLE functions, to override the standard behavior of those functions.

- When a table is marked as SHADOWCLUSTER, it is marked internally as a "shadow" table expression so that it is only enabled in an ALLSELECTED context.


## Related content

[Filter functions](filter-functions-dax.md)  
[GROUPCROSSAPPLY function](groupcrossapply-function-dax.md)  
[GROUPCROSSAPPLYTABLE function](groupcrossapplytable-function-dax.md)  
