---
title: "DEFINE keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 03/27/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# DEFINE
  
A keyword that defines entities that can be applied to one or more EVALUATE statements of a [DAX query](dax-queries.md).

## Syntax  
  
```dax
DEFINE {  <entity> [<name>] = <expression> }
```
  
### Arguments
  
|Term|Definition|  
|--------|--------------|  
|entity|MEASURE, VAR, TABLE, or COLUMN.|
|name|The name of an entity. It cannot be an expression.|  
|expression|Any DAX expression that returns a single scalar value. The expression can use any of the defined entities. The expression must return a table. If a scalar value is required, wrap the scalar inside a ROW() function to produce a table.|  
  
## Remarks

Entities can be variables, measures, tables, and columns.

Definitions typically precede the EVALUATE statement and are valid for all EVALUATE statements.

Definitions can reference other definitions that appear before or after the current definition.

Definitions exist only for the duration of the query.

## See also

[DAX queries](dax-queries.md)   
[ORDER BY](orderby-statement-dax.md)   
[VAR](var-dax.md)   