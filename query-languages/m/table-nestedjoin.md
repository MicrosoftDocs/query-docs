---
title: "Table.NestedJoin | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.NestedJoin

## Syntax

<pre>
Table.NestedJoin(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as any, <b>key2</b> as any, <b>newColumnName</b> as text, optional <b>joinKind</b> as nullable number, optional <b>keyEqualityComparers</b> as nullable list) as table
</pre>

## About
<p>Joins the rows of `table1` with the rows of `table2` based on the equality of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`). The results are entered into the column named `newColumnName`.</p> <p>The optional `joinKind` specifies the kind of join to perform. By default, a left outer join is performed if a `joinKind` is not specified.</p> <p>An optional set of `keyEqualityComparers` may be included to specify how to compare the key columns.</p> 