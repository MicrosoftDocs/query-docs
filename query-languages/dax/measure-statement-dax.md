---
description: "Learn more about: MEASURE"
title: "MEASURE keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/16/2022
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend 
recommendations: false

---
# MEASURE


## Syntax

```dax
[DEFINE 
    (
     (MEASURE <table name>[<measure name>] = <scalar expression>)
    ) + 
]

(EVALUATE <table expression>) +
```

## Arguments

|Term  |Definition  |
|---------|---------|
|  table name     |     |
|  measure name     |  The name of the measure. It cannot be an expression. The name does not have to be unique. The name exists only for the duration of the query.   |
|  scalar expression     | A DAX expression that returns a scalar value.  |

## Remarks

- Measure definitions for a query override model measures of the same name.

- The expression for a measure definition can be used with any other expression in the same query.

## Example

```dax

```

## See also

[DEFINE](define-statement-dax.md)  
[EVALUATE](evaluate-statement-dax.md)  
[VAR](var-dax.md)  
[DAX queries](dax-queries.md)  
