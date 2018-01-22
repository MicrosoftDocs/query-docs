---
title: "RowExpression.Column | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a6369816-aa24-4285-bf40-3678db431758
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# RowExpression.Column
RowExpression.Column(columnName as text) as record  
  
## About  
Returns an AST that represents access to column columnName of the row within a row expression.  
  
### Example 1  
Creates an AST representing access of column "CustomerName".  
  
```  
RowExpression.Column("CustomerName")  
```  
