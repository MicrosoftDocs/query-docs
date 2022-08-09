---
description: "Learn more about: START AT"
title: "START AT keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/09/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# START AT
  
A keyword used inside an ORDER BY clause within an EVALUATE statement. START AT defines the value at which query results begin.

## Syntax  
  
```dax
[START AT {<value>|<parameter>} [, …]]]  
```
  
### Arguments
  
|Term|Definition|  
|--------|--------------|  
|measureName|The name of the measure. Exists only for the duration of the query.|
|expression|Any DAX expression that returns a single scalar value. The expression can use any other defined entities. The expression must return a table. If a scalar value is required, wrap the scalar inside a ROW() function to produce a table.|  
  
## Remarks

- Measures defined for a query exist only for the duration of a the query.

- Measures defined for a query override model measures of the same name.

- The expression for a defined measure can be used can be used with any other expression in the same query.

## Examples

DEFINE
    MEASURE Product[# Unique Products] = DISTINCTCOUNT ( Product[ProductKey] )

## See also

[DAX queries](dax-queries.md)  
[EVALUATE](evaluate-statement.md)  
[VAR](var-dax.md)  
