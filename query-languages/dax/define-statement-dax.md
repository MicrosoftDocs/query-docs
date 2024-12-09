---
description: "Learn more about: DEFINE"
title: "DEFINE keyword (DAX)"
---
# DEFINE
  
Introduces a statement with one or more entity definitions that can be applied to one or more EVALUATE statements of a [DAX query](dax-queries.md).

## Syntax  
  
```dax
[DEFINE 
    (
     (MEASURE <table name>[<measure name>] = <scalar expression>) | 
     (VAR <var name> = <table or scalar expression>) |
     (TABLE <table name> = <table expression>) | 
     (COLUMN <table name>[<column name>] = <scalar expression>) | 
    ) + 
]

(EVALUATE <table expression>) +
```
  
### Parameters
  
|Term|Definition|  
|--------|--------------|  
|`Entity`|MEASURE, VAR, TABLE<sup>[1](#not-rec)</sup>, or COLUMN<sup>[1](#not-rec)</sup>. |
|`name`|The name of a measure, var, table, or column definition. It cannot be an expression. The name does not have to be unique. The name exists only for the duration of the query.|  
|`expression`|Any DAX expression that returns a table or scalar value. The expression can use any of the defined entities. If there is a need to convert a scalar expression into a table expression, wrap the expression inside a table constructor with curly braces `{}`, or use the `ROW()` function to return a single row table.|

<a name="not-rec">[1]</a> **Caution:** Query scoped TABLE and COLUMN definitions are meant for internal use only. While you can define TABLE and COLUMN expressions for a query without syntax error, they may produce runtime errors and are not recommended.

## Remarks

- A DAX query can have multiple EVALUATE statements, but can have only one DEFINE statement. Definitions in the DEFINE statement can apply to any EVALUATE statements in the query.

- At least one definition is required in a DEFINE statement.

- Measure definitions for a query override model measures of the same name.

- VAR names have unique restrictions. To learn more, see [VAR - Parameters](var-dax.md#parameters).

- To learn more about how a DEFINE statement is used, see [DAX queries](dax-queries.md).

## Related content

[EVALUATE](evaluate-statement-dax.md)  
[VAR](var-dax.md)  
[MEASURE](measure-statement-dax.md)  
[DAX queries](dax-queries.md)
