---
title: "RowExpression.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 50ebce17-136d-43f5-b3a6-c77a9e8ec116
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# RowExpression.From
RowExpression.From(function as function) as record  
  
## About  

Returns the AST for the body of <code>function</code>, normalized into a *row expression*:

* The function must be a 1-argument lambda.
* All references to the function parameter are replaced with <code>RowExpression.Row</code>.
* All references to columns are replaced with <code>RowExpression.Column(*columnName*)</code>. 
* The AST will be simplified to contain only nodes of the kinds: 
<code>Constant</code>,
<code>Invocation</code>,
<code>Unary</code>,
<code>Binary</code>,
<code>If</code>,
<code>FieldAccess</code>,
<code>NotImplemented</code>.

* An error is raised if a row expression AST cannot be returned for the body of <code>function</code>.
  
### Example 1  
Returns the AST for the body of the function each [CustomerID] = "ALFKI"  
  
```  
RowExpression.From(each [CustomerName] = "ALFKI")  
```  
