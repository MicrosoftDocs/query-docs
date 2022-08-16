---
description: "Learn more about: DEFINE"
title: "DEFINE keyword (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.subservice: dax 
ms.date: 08/16/2022
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
[DEFINE 
    (
     (MEASURE <table name>[<measure name>] = <scalar expression>) | 
     (VAR <var name> = <table or scalar expression>) |
     (TABLE <table name> = <table expression>) | 
     (COLUMN <table name>[column name] = <scalar expression>) | 
    ) + 
]

(EVALUATE <table expression>) +
```
  
### Arguments
  
|Term|Definition|  
|--------|--------------|  
|Entity|MEASURE, VAR, TABLE<sup>[1](#not-rec)</sup>, or COLUMN<sup>[1](#not-rec)</sup>. |
|name|The name of a measure, var, table, or column definition. It cannot be an expression. The name does not have to be unique. The name exists only for the duration of the query.|  
|expression|Any DAX expression that returns a table or scalar value. The expression can use any of the defined entities. If a scalar value is required, wrap the expression inside a table constructor with curly braces `{}`, or use the `ROW()` function to return a single row table.|

<a name="not-rec">[1]</a> **Caution:** Query scoped TABLE and COLUMN definitions are meant for internal use only. User defined TABLE and COLUMN definitions may return inconsistent results and are not recommended.

## Remarks

- At least one definition is required in a DEFINE statement.

- Measure definitions for a query override model measures of the same name.

- The expression for a measure definition can be used with any other expression in the same query.

- VAR names have unique  restrictions. To learn more, see [VAR - Parameters](var-dax.md#parameters).

## Example

```DAX
DEFINE
    MEASURE Products[Number of products] = DISTINCTCOUNT ( Products[Product]) 
```

Defines a measure named Number of Products that calculates the distinct count of products.

## See also

[EVALUATE](evaluate-statement-dax.md)  
[VAR](var-dax.md)  
[MEASURE](measure-statement-dax.md)  
[DAX queries](dax-queries.md)  