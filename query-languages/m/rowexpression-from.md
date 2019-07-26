---
title: "RowExpression.From | Microsoft Docs"
ms.date: 7/26/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# RowExpression.From

## Syntax

<pre>
RowExpression.From(<b>function</b> as function) as record
</pre>  
  
## About  

Returns the AST for the body of <code>function</code>, normalized into a <i>row expression</i>: <ul> <li>The function must be a 1-argument lambda.</li> <li>All references to the function parameter are replaced with <code>RowExpression.Row</code>.</li> <li>All references to columns are replaced with <code>RowExpression.Column(<i>columnName</i>)</code>.</li> <li>The AST will be simplified to contain only nodes of the kinds: <ul> <li><code>Constant</code></li> <li><code>Invocation</code></li> <li><code>Unary</code></li> <li><code>Binary</code></li> <li><code>If</code></li> <li><code>FieldAccess</code></li> <li><code>NotImplemented</code></li> </ul> </li> </ul> </p> </p>An error is raised if a row expression AST cannot be returned for the body of <code>function</code>.
  
### Example 1  
Returns the AST for the body of the function each [CustomerID] = "ALFKI"  
  
```powerquery-m
RowExpression.From(each [CustomerName] = "ALFKI")  
```  

<table> <tr> <th>Kind</th> <td>Binary</td> </tr> <tr> <th>Operator</th> <td>Equals</td> </tr> <tr> <th>Left</th> <td>[Record]</td> </tr> <tr> <th>Right</th> <td>[Record]</td> </tr> </table>

