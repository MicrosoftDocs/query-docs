---
description: "Learn more about: Value.NativeQuery"
title: "Value.NativeQuery | Microsoft Docs"
ms.date: 11/17/2021
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Value.NativeQuery

## Syntax

<pre>Value.NativeQuery(<b>target</b> as any, <b>query</b> as text, optional <b>parameters</b> as any, optional <b>options</b> as nullable record) as any
</pre>

## About

Evaluates `query` against `target` using the parameters specified in `parameters` and the options specified in `options`.

The output of the query is defined by `target`.

`target` provides the context for the operation described by `query`.

`query` describes the query to be executed against `target`. `query` is expressed in a manner specific to `target` (for example, a T-SQL statement).

The optional `parameters` value may contain either a list or record as appropriate to supply the parameter values expected by `query`.

The optional `options` record may contain options that affect the evaluation behavior of `query` against `target`. These options are specific to `target`.
