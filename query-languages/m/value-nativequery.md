---
title: "Value.NativeQuery | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.NativeQuery
<code>Value.NativeQuery(<b>target</b> as any, <b>query</b> as text, optional <b>parameters</b> as any, optional <b>options</b> as nullable record) as any</code>
## About

Evaluates <code>query</code> against <code>target</code> using the parameters specified in <code>parameters</code> and the options specified in <code>options</code>.

The output of the query is defined by <code>target</code>.

<code>target</code> provides the context for the operation described by <code>query</code>.

<code>query</code> describes the query to be executed against <code>target</code>. <code>query</code> is expressed in a manner specific to <code>target</code> (e.g. a T-SQL statement).

The optional <code>parameters</code> value may contain either a list or record as appropriate to supply the parameter values expected by <code>query</code>.

The optional <code>options</code> record may contain options that affect the evaluation behavior of <code>query</code> against <code>target</code>. These options are specific to <code>target</code>.



  
