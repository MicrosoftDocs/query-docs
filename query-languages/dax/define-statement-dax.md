---
description: "Learn more about: DEFINE"
title: "DEFINE keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 07/05/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# DEFINE
  
A keyword that defines entities that can be applied to one or more EVALUATE statements of a [DAX query](dax-queries.md).

## Syntax  
  
```dax
DEFINE 
    <entity> <name> = <expression>
```
  
### Arguments
  
|Term|Definition|  
|--------|--------------|  
|entity|MEASURE, VAR, TABLE\*, or COLUMN\*. |
|name|The name of an entity. It cannot be an expression.|  
|expression|Any DAX expression that returns a single scalar value. The expression can use any of the defined entities. The expression must return a table. If a scalar value is required, wrap the scalar inside a ROW() function to produce a table.|  
  
## Remarks

- *Table and column entity types are currently for internal use only. Functionality for these entity types is subject to change.

- Definitions typically precede the EVALUATE statement and are valid for all EVALUATE statements for the duration of the query.

- Definitions can reference other definitions that appear before or after the current definition.

## Examples

```DAX
DEFINE
    MEASURE Customer[# Customers] = COUNTROWS ( Customer )
    MEASURE Product[Number of products] = DISTINCTCOUNT ( Product[Product]) 
```



## See also

[DAX queries](dax-queries.md) 
[VAR](var-dax.md)  
[ORDER BY](orderby-statement-dax.md)  
