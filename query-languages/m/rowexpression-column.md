---
description: "Learn more about: RowExpression.Column"
title: "RowExpression.Column | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# RowExpression.Column

## Syntax

<pre>
RowExpression.Column(<b>columnName</b> as text) as record
</pre>
  
## About

Returns an AST that represents access to column `columnName` of the row within a row expression.  
  
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
