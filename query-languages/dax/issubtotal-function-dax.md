---
title: "ISSUBTOTAL function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ISSUBTOTAL

Creates another column in a [SUMMARIZE](summarize-function-dax.md) expression that returns True if the row contains sub-total values for the column given as argument, otherwise returns False.

## Syntax  
  
```dax
ISSUBTOTAL(<columnName>)
```

With [SUMMARIZE](summarize-function-dax.md),

```dax
SUMMARIZE(<table>, <groupBy_columnName>[, <groupBy_columnName>]…[, ROLLUP(<groupBy_columnName>[,< groupBy_columnName>…])][, <name>, {<expression>|ISSUBTOTAL(<columnName>)}]…)  
```
  
### Parameters  

|Term|Definition|  
|--------|--------------|
|columnName  |The name of any column in table of the SUMMARIZE function or any column in a related table to table.  |

## Return value

A **True** value if the row contains a sub-total value for the column given as argument, otherwise returns **False**.
  
## Remarks  

- This function can only be used in the expression of a [SUMMARIZE](summarize-function-dax.md) function.

- This function must be preceded by a matching name column.

## Example

See [SUMMARIZE](summarize-function-dax.md).
