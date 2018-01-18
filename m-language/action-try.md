---
title: "Action.Try | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 60337229-4aa1-4fee-abe3-20835db8c9aa
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Action.Try
<code>Action.Try(<b>action</b> as action) as action</code>  
## About  
Creates an action that executes <code>action</code>, catches any errors that occur while executing the action, and returns a record containing a <code>HasError</code> field and either a <code>Value</code> or <code>Error</code> field depending on whether the action executed successfully.  
  
## Example 1  
<p>Creates an action that will try the execution of a second action that throws an error. The result of the <code>Try</code> action is the error record:</p> <p><code>[HasError = true, Error = [Reason = "Expression.Error", Message = "Error!", Detail = null]</code></p>  
  
<code>Action.Try(Action.Sequence({() => Action.Return(error "Error!")}))</code>  
  
<code>action</code>  
  
## Example 2  
<p>Creates an action that will try the execution of a second action that returns a result. The result of the <code>Try</code> action is a success record:</p> <p><code>[HasError = false, Value = "Success!"]</code></p>   
  
<code>Action.Try(Action.Sequence({() => Action.Return("Success!")}))</code>  
  
<code>action</code>  
