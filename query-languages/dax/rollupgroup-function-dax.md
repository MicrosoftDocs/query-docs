---
description: "Learn more about: ROLLUPGROUP"
title: "ROLLUPGROUP function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 09/09/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# ROLLUPGROUP

Modifies the behavior of the [SUMMARIZE](summarize-function-dax.md) and [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) functions by adding rollup rows to the result on columns defined by the the groupBy_columnName parameter. This function can only be used within a [SUMMARIZE](summarize-function-dax.md) or [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.
  
## Syntax  
  
```dax
ROLLUPGROUP ( <groupBy_columnName> [, <groupBy_columnName> [, … ] ] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| groupBy_columnName | The qualified name of an existing column or ROLLUPGROUP function to be used to create summary groups based on the values found in it. This parameter cannot be an expression.  |

## Return value

This function does not return a value. It marks a set of columns to be treated as a single group during subtotaling by [ROLLUP](rollup-function-dax.md) or [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md).
  
## Remarks  
  
ROLLUPGROUP can only be used as a groupBy_columnName argument to [ROLLUP](rollup-function-dax.md), [ROLLUPADDISSUBTOTAL](rollupaddissubtotal-function-dax.md), or [ROLLUPISSUBTOTAL](rollupissubtotal-function-dax.md).

## Example

See [SUMMARIZE](summarize-function-dax.md) and [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
