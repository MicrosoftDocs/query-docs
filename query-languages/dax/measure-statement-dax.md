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

Introduces a measure definition in a DEFINE statement of a [DAX query](dax-queries.md).

## Syntax

```dax
[DEFINE 
    (
      MEASURE <table name>[<measure name>] = <scalar expression>
    ) + 
]

(EVALUATE <table expression>) +
```

## Parameters

|Term  |Definition  |
|---------|---------|
|  table name     |   The name of a table containing the measure.  |
|  measure name     |  The name of the measure. It cannot be an expression. The name does not have to be unique. The name exists only for the duration of the query.   |
|  scalar expression     | A DAX expression that returns a scalar value.  |

## Remarks

- Measure definitions for a query override model measures of the same name for the duration of the query. They will not affect the model measure.

- The expression for a measure definition can be used with any other expression in the same query.

- To learn more about how MEASURE statements are used, see [DAX queries](dax-queries.md).

## See also

[DEFINE](define-statement-dax.md)  
[EVALUATE](evaluate-statement-dax.md)  
[VAR](var-dax.md)  
[DAX queries](dax-queries.md)  
