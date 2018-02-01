---
title: "Table.View | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2313f8a2-2bcd-443d-9d24-1f714bd254c7
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.View
<code>Table.View(<b>table</b> as nullable table, <b>handlers</b> as record) as table</code>

## About

Returns a view of <code>table</code> where the functions specified in <code>handlers</code> are used in lieu of the default behavior of an operation when the operation is applied to the view.
Handler functions are optional. If a handler function is not specified for an operation, the default behavior of the operation is applied to <code>table</code> instead (except in the case of <code>GetExpression</code>).

Handler functions must return a value that is semantically equivalent to the result of applying the operation against <code>table</code> (or the resulting view in the case of <code>GetExpression</code>).

If a handler function raises an error, the default behavior of the operation is applied to the view.

<code>Table.View</code> can be used to implement folding to a data source – the translation of M queries into source-specific queries (e.g. to create T-SQL statements from M queries).

Please see the published documentation for a more complete description of <code>Table.View</code>.
  
