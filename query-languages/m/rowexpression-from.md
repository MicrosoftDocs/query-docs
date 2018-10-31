---
title: "RowExpression.From | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RowExpression.From
`RowExpression.From(<b>function</b> as function) as record`  
  
## About  

Returns the AST for the body of `function`, normalized into a *row expression*:

* The function must be a 1-argument lambda.
* All references to the function parameter are replaced with `RowExpression.Row`.
* All references to columns are replaced with `RowExpression.Column(*columnName*)`. 
* The AST will be simplified to contain only nodes of the kinds: 
`Constant`,
`Invocation`,
`Unary`,
`Binary`,
`If`,
`FieldAccess`,
`NotImplemented`.

* An error is raised if a row expression AST cannot be returned for the body of `function`.
  
### Example 1  
Returns the AST for the body of the function each [CustomerID] = "ALFKI"  
  
```  
RowExpression.From(each [CustomerName] = "ALFKI")  
```  
