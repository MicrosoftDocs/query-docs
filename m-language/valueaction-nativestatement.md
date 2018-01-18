---
title: "ValueAction.NativeStatement | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
applies_to: 
  - "Power BI"
ms.assetid: 7c6c6133-e788-4a3f-85f7-c5df9a8d9cbd
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# ValueAction.NativeStatement
<code>ValueAction.NativeStatement(<b>target</b> as any, <b>statement</b> as text, optional <b>parameters</b> as any, optional <b>options</b> as nullable record) as action</code>

## About

Creates an action that executes <code>statement</code> against <code>target</code> using the parameters specified in <code>parameters</code> and the options specified in <code>options</code>.

The behavior of the created action is defined by <code>target</code>.

<code>target</code> provides the context for the operation described by <code>statement</code>.

<code>statement</code> describes the action to be taken against <code>target</code>. <code>statement</code> is expressed in a manner specific to <code>target</code> (e.g. a T-SQL statement).

The optional <code>parameters</code> value may contain either a list or record as appropriate to supply the parameter values expected by <code>statement</code>.

The optional <code>options</code> record may contain options that affect the execution behavior of <code>statement</code> against <code>target</code>. These options are specific to <code>target</code>.

The returned action will perform the described operation when executed. The action returns a meaningful value representing the outcome of the operation (e.g. a status code, the number of rows affected, etc.).

The function will raise an evaluation error if invalid input arguments are detected (before trying to perform the operation).

The action will raise an execution error if the operation cannot be successfully completed.

<b>NOTE:</b> <code>target</code> may be left in an undefined state if an execution error occurs.
  
