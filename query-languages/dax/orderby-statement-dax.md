---
title: "ORDER BY keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 03/27/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# ORDER BY
  
Defines the sort oder of query results returned by an EVALUATE statement in a [DAX query](dax-queries.md).

## Syntax  
  
```dax
ORDER BY {<expression> [{ASC | DESC}]}
```
  
### Arguments
  
|Term|Definition|  
|--------|--------------|  
|expression|Any DAX expression that returns a single scalar value.|  
|ASC|(default) Ascending sort order.|  
|DESC|Descending sort order.|  
  
## Return value

The result of an EVALUATE statement in ascending (ASC) or descending (DESC) order.

## Example

```dax
EVALUATE(
    'Internet Sales'
    )
ORDER BY
    'Internet Sales'[Order Date]
```

Returns all rows and columns from the Internet Sales table, ordered by Order Date, as a table.
  
## See also

[DAX queries](dax-queries.md)