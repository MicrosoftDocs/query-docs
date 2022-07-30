---
description: "Learn more about: RowExpression.From"
title: "RowExpression.From"
ms.date: 3/16/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# RowExpression.From

## Syntax

<pre>
RowExpression.From(<b>function</b> as function) as record
</pre>  
  
## About  

Returns the abstract syntax tree (AST) for the body of `function`, normalized into a _row expression_:

* The function must be a 1-argument lambda.
* All references to the function parameter are replaced with `RowExpression.Row`.
* All references to columns are replaced with <code>RowExpression.Column(_columnName_)</code>.
* The AST will be simplified to contain only nodes of the kinds:
  * `Constant`
  * `Invocation`
  * `Unary`
  * `Binary`
  * `If`
  * `FieldAccess`
  * `NotImplemented`

An error is raised if a row expression AST cannot be returned for the body of `function`.
  
## Example 1

Returns the AST for the body of the function each [CustomerID] = "ALFKI"

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
