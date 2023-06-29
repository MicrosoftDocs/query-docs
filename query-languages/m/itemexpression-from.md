---
description: "Learn more about: ItemExpression.From"
title: "ItemExpression.From"
ms.date: 6/15/2023
---
# ItemExpression.From

## Syntax

<pre>
ItemExpression.From(<b>function</b> as function) as record
</pre>

## About

Returns the abstract syntax tree (AST) for the body of `function`, normalized into an *item expression*:

* The function must be a 1-argument lambda.
* All references to the function parameter are replaced with [ItemExpression.Item](itemexpression-item.md).
* The AST will be simplified to contain only nodes of the kinds:
  * `Constant`
  * `Invocation`
  * `Unary`
  * `Binary`
  * `If`
  * `FieldAccess`

An error is raised if an item expression AST cannot be returned for the body of `function`.

This function is identical to [`RowExpression.From`](rowexpression-from.md).

## Example 1

Returns the AST for the body of the function `each _ <> null`.

**Usage**

```powerquery-m
ItemExpression.From(each _ <> null)
```

**Output**

```powerquery-m
[
    Kind = "Binary",
    Operator = "NotEquals",
    Left = ItemExpression.Item,
    Right =
    [
        Kind = "Constant",
        Value = null
    ]
]
```
