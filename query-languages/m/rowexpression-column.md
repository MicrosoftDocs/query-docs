---
title: "RowExpression.Column | Microsoft Docs"
ms.date: 7/26/2019
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

<table> <tr> <th>Kind</th> <td>FieldAccess</td> </tr> <tr> <th>Expression</th> <td>[Record]</td> </tr> <tr> <th>MemberName</th> <td>CustomerName</td> </tr> </table>
