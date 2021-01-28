---
description: "Learn more about: NONVISUAL"
title: "NONVISUAL function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# NONVISUAL

Marks a value filter in a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression as non-visual. This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.

## Syntax  
  
```dax
NONVISUAL(<expression>)
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|expression|Any DAX expression that returns a single value (not a table).|

## Return value

A table of values.
  
## Remarks  

- Marks a value filter in [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) as not affecting measure values, but only applying to group-by columns.

- This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression. It's used as either a filterTable argument of the [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) function or a groupLevelFilter argument of the [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md) or [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md) function.

## Example

See [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
