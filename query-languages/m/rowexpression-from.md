---
description: "Learn more about: RowExpression.From"
title: "RowExpression.From"
---
# RowExpression.From

## Syntax

<pre>
RowExpression.From(<b>function</b> as function) as record
</pre>  

## About

Returns the abstract syntax tree (AST) for the body of `function`, normalized into a _row expression_:

* The function must be a 1-argument lambda.
* All references to the function parameter are replaced with [`RowExpression.Row`](rowexpression-row.md).
* All references to columns are replaced with [`RowExpression.Column(columnName)`](rowexpression-column.md).
* The AST will be simplified to contain only nodes of the kinds:
  * `Constant`
  * `Invocation`
  * `Unary`
  * `Binary`
  * `If`
  * `FieldAccess`

An error is raised if a row expression AST cannot be returned for the body of `function`.

This function is identical to [`ItemExpression.From`](itemexpression-from.md).
  
## Example 1

Returns the AST for the body of the function `each [CustomerID] = "ALFKI"`.

**Usage**
  
```powerquery-m
RowExpression.From(each [CustomerName] = "ALFKI")  
```  

**Output**

```powerquery-m
[
    Kind = "Binary",
    Operator = "Equals",
    Left = RowExpression.Column("CustomerName"),
    Right =
    [
        Kind = "Constant",
        Value = "ALFKI"
    ]
]
```
