---
title: "CURRENTGROUP function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# CURRENTGROUP

Returns a set of rows from the table argument of a [GROUPBY](groupby-function-dax.md) expression that belong to the current row of the [GROUPBY](groupby-function-dax.md) result.

## Syntax  
  
```dax
CURRENTGROUP ( )
```
  
### Parameters  
  
None
  
## Return value

A table with the selected columns for the groupBy_columnName arguments and the grouped by columns designated by the name arguments.  
  
## Remarks

This function takes no arguments and is only supported as the first argument to one of the following aggregation functions: AVERAGEX, COUNTAX, COUNTX, GEOMEANX, MAXX, MINX, PRODUCTX, STDEVX.S, STDEVX.P, SUMX, VARX.S, VARX.P.
  
## Example

See [GROUPBY](groupby-function-dax.md).
