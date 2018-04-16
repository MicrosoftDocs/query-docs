---
title: "RowExpression.From | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RowExpression.From
<code>RowExpression.From(<b>function</b> as function) as record</code>  
  
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
