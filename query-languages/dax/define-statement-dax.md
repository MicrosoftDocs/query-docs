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
     (COLUMN <table name>[<column name>] = <scalar expression>) |
     (FUNCTION <function name> = ([parameter name]: [parameter type], ...) => <function body>) |
     (MEASURE <table name>[<measure name>] = <scalar expression>) | 
     (TABLE <table name> = <virtual table definition>) | 
     (VAR <var name> = <table or scalar expression>) |
    ) + 
]

(EVALUATE <table expression>) +
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Entity`|COLUMN<sup>[1](#not-rec)</sup>, FUNCTION, MEASURE, TABLE<sup>[1](#not-rec)</sup>, or VAR.|
|`name`|The name of a column, function, measure, table, or var definition. It cannot be an expression. The name does not have to be unique. The name exists only for the duration of the query.|
|`expression`|Any DAX expression that returns a table or scalar value. The expression can use any of the defined entities. If there is a need to convert a scalar expression into a table expression, wrap the expression inside a table constructor with curly braces `{}`, or use the `ROW()` function to return a single row table.|
|`parameter type`, `parameter name`, `function body`|See [FUNCTION statement](function-statement-dax.md).|

<a name="not-rec">[1]</a> **Caution:** Query scoped TABLE and COLUMN definitions are meant for internal use only. While you can define TABLE and COLUMN expressions for a query without syntax error, they may produce runtime errors and are not recommended.

## Remarks

- A DAX query can have multiple EVALUATE statements, but can have only one DEFINE statement. Definitions in the DEFINE statement can apply to any EVALUATE statements in the query.

- At least one definition is required in a DEFINE statement.

- Measure definitions for a query override model measures of the same name.

- VAR names have unique restrictions. To learn more, see [VAR - Parameters](var-dax.md#parameters).

- To learn more about how a DEFINE statement is used, see [DAX queries](dax-queries.md).

- To learn more about virtual column, see [Virtual Column](virtual-column-statement-dax.md)

- To learn more about virtual table, see [Virtual Table](virtual-table-statement-dax.md)

- To learn more about DAX user defined functions, see [DAX User Defined Functions](function-statement-dax.md)

## Related content

- [EVALUATE](evaluate-statement-dax.md)  
- [FUNCTION](function-statement-dax.md)
- [VAR](var-dax.md)  
- [MEASURE](measure-statement-dax.md)  
- [Virtual Column](virtual-column-statement-dax.md)
- [Virtual Table](virtual-table-statement-dax.md)
- [DAX queries](dax-queries.md)
