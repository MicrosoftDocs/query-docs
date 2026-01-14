---
description: "Learn more about: RowExpression.Column"
title: "RowExpression.Column"
ms.subservice: m-source
ms.topic: reference
---
# RowExpression.Column

## Syntax

<pre>
RowExpression.Column(<b>columnName</b> as text) as record
</pre>
  
## About

Returns an abstract syntax tree (AST) that represents access to column `columnName` of the row within a row expression.  
  
## Example 1

Creates an AST representing access of column "CustomerName".

**Usage**
  
```powerquery-m
RowExpression.Column("CustomerName")  
```

**Output**

```powerquery-m
[
    Kind = "FieldAccess",
    Expression = RowExpression.Row,
    MemberName = "CustomerName"
]
```
