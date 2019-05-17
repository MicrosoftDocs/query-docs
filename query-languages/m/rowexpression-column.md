---
title: "RowExpression.Column | Microsoft Docs"
ms.date: 5/17/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RowExpression.Column

## Syntax

<pre>
RowExpression.Column(<b>columnName</b> as text) as record
</pre>
  
## About  
Returns an AST that represents access to column columnName of the row within a row expression.  
  
### Example 1  
Creates an AST representing access of column "CustomerName".  
  
```powerquery-m
RowExpression.Column("CustomerName")  
```  

<code>[ Kind = "FieldAccess", Expression = RowExpression.Row, MemberName = "CustomerName" ]</code>