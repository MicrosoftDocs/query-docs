---
title: "ROLLUPGROUP function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ROLLUPGROUP

Modifies the behavior of the [SUMMARIZE](summarize-function-dax.md) and [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) functions by adding roll-up rows to the result on columns defined by the the groupBy_columnName parameter. This function can only be used within a [SUMMARIZE](summarize-function-dax.md) or [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.
  
## Syntax  
  
```dax
ROLLUPGROUP ( <groupBy_columnName> [, <groupBy_columnName> [, … ] ] )
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
| groupBy_columnName | The qualified name of an existing column to be used to create summary groups based on the values found in it. This parameter cannot be an expression.  |

## Return value

The function does not return a value. It marks a set of columns to be grouped during subtotaling by ROLLUPADDISSUBTOTAL.
  
## Remarks  
  
ROLLUPGROUP can only be used as an groupBy_columnName argument to ROLLUPADDISSUBTOTAL or the SUMMARIZE function.

## Example

See [SUMMARIZE](summarize-function-dax.md) and [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).

