---
title: "Action.Sequence | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3e84db63-f420-424a-a38e-a7b7214f00b7
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Action.Sequence
<code>Action.Sequence(<b>actions</b> as list) as action</code>  
## About  
<p>Creates an action that executes the sequence of elements in <code>actions</code> in order.</p> <p>Each element of <code>actions</code> is either an action or a function that returns an action. An element in the list is executed only after all of the elements preceding it in the list are executed. In the case of an element that is a function, "executed" means that the function is evaluated and the action it returns is executed.</p> <p>If an element of the list is a function then it must be either a 0 or 1-argument function that returns an action. The result of the execution of the preceding element is provided as the input to the function if it is a 1-argument function. The initial result (i.e. the result available to the first function in the sequence) is <code>null</code>. </p> <p>Any element in the list that depends on a side effect or result of executing a preceding element must be expressed using a function.</p> <p>The result of <code>Action.Sequence</code> is the result of executing the last element in the list (or <code>null</code> if the sequence is empty).</p> <p><b>NOTE:</b> A function in the list is not guaranteed to observe the side effects from the execution of the preceding elements in the list if the function references variables declared outside of its body (due to capture of free variables when the function is constructed). To ensure that updated data is observed by the function after an earlier element in the list executes, use an expression or function that directly accesses the affected data sources.</p>  
  
## Example 1  
Creates an action that, when executed, will execute the first action (which returns <code>"hello"</code>), combine its result with the string <code>"world!"</code> to create a second action, and then execute the second action to produce a result of <code>"hello world!"</code>.  
  
<code>Action.Sequence({ Action.Return("Hello"), (result) => Action.Return(result & " " & "world!") })</code>  
  
<code>action</code>  
