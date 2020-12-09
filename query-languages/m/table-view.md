---
title: "Table.View | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.View

## Syntax

<pre>
Table.View(<b>table</b> as nullable table, <b>handlers</b> as record) as table
</pre>

## About

Returns a view of `table` where the functions specified in `handlers` are used in lieu of the default behavior of an operation when the operation is applied to the view.
Handler functions are optional. If a handler function is not specified for an operation, the default behavior of the operation is applied to `table` instead (except in the case of `GetExpression`).

Handler functions must return a value that is semantically equivalent to the result of applying the operation against `table` (or the resulting view in the case of `GetExpression`).

If a handler function raises an error, the default behavior of the operation is applied to the view.

`Table.View` can be used to implement folding to a data source – the translation of M queries into source-specific queries (e.g. to create T-SQL statements from M queries).

Please see the published documentation for a more complete description of `Table.View`.
  
