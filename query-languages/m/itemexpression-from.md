---
description: "Learn more about: ItemExpression.From"
title: "ItemExpression.From"
ms.date: 3/16/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# ItemExpression.From

## Syntax

<pre>
ItemExpression.From(<b>function</b> as function) as record
</pre>

## About

Returns the abstract syntax tree (AST) for the body of `function`, normalized into an *item expression*:

- The function must be a 1-argument lambda.
- All references to the function parameter are replaced with `ItemExpression.Item`.
- The AST will be simplified to contain only nodes of the kinds:
  - `Constant`
  - `Invocation`
  - `Unary`
  - `Binary`
  - `If`
  - `FieldAccess`
  - `NotImplemented`

An error is raised if an item expression AST cannot be returned for the body of `function`.

## Example 1

Returns the AST for the body of the function `each _ <> null`

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
