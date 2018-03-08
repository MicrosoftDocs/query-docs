---
title: "ItemExpression.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 89983331-e946-4341-8f6d-fc251733c9fd
caps.latest.revision: 2
author: "MarkMcGeeAtAquent"
ms.author: "v-mamcge"
manager: "kfile"
---
# ItemExpression.From
<code>ItemExpression.From(<b>function</b> as function) as record</code>

## About
Returns the AST for the body of `function`, normalized into an *item expression*: 

- The function must be a 1-argument lambda. 
- All references to the function parameter are replaced with `ItemExpression.Item`. 
- The AST will be simplified to contain only nodes of the kinds: 
  - `Constant` 
  - `Invocation` 
  - `Unary` 
  - `Binary` 
  - `If` 
  - `FieldAccess` 
  - `NotImplemented`    

An error is raised if an item expression AST cannot be returned for the body of `function`.

## Example 1
Returns the AST for the body of the function `each _ <> null`

`ItemExpression.From(each _ <> null)`


<table> <tr> <th>Kind</th> <td>Binary</td> </tr> <tr> <th>Operator</th> <td>NotEquals</td> </tr> <tr> <th>Left</th> <td>[Record]</td> </tr> <tr> <th>Right</th> <td>[Record]</td> </tr> </table>

