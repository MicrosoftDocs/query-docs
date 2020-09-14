---
title: "IGNORE function (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 09/01/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# IGNORE

Modifies the behavior of the [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) function by omitting specific expressions from the BLANK/NULL evaluation. Rows for which all expressions not using IGNORE return BLANK/NULL will be excluded independent of whether the expressions which do use IGNORE evaluate to BLANK/NULL or not. This function can only be used within a [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md) expression.
  
## Syntax  
  
```dax
IGNORE(<expression>)
```

With SUMMARIZECOLUMNS,
  
```dax
SUMMARIZECOLUMNS(<groupBy_columnName>[, < groupBy_columnName >]…, [<filterTable>]…[, <name>, IGNORE(…)]…)
```  
  
### Parameters  

|Term|Definition|  
|--------|--------------|  
|expression|Any DAX expression that returns a single value (not a table).|

## Return value

The function does not return a value.
  
## Remarks  

IGNORE can only be used as an expression argument to [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).  

## Example

See [SUMMARIZECOLUMNS](summarizecolumns-function-dax.md).
