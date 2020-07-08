---
title: "EVALUATE keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/08/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# EVALUATE
  
A statement containing a table expression required in a [DAX query](dax-queries.md).

## Syntax  
  
```dax
EVALUATE <table>  
```
  
### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|table|A table expression|  
  
## Return value

The result of a table expression.

## Remarks

A query can contain multiple EVALUATE statements.

## Example

```dax
EVALUATE(
    'Internet Sales'
    )
```

Returns all rows and columns from the Internet Sales table, as a table.
  
## See also

[DAX queries](dax-queries.md)  
[DEFINE](define-statement-dax.md)  
[ORDER BY](orderby-statement-dax.md)
