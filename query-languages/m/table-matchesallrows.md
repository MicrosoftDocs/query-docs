---
title: "Table.MatchesAllRows | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.MatchesAllRows

## Syntax

<pre>
Table.MatchesAllRows(<b>table</b> as table, <b>condition</b> as function) as logical 
</pre>
  
## About  
Indicates whether all the rows in the `table` match the given `condition`. Returns `true` if all of the rows match, `false` otherwise.

## Example 1
Determine whether all of the row values in column [a] are even in the table.

```powerquery-m
Table.MatchesAllRows(Table.FromRecords({[a = 2, b = 4], [a = 6, b = 8]}), each Number.Mod([a], 2) = 0 )
```

`true`

## Example 2
Find if all of the row values are [a = 1, b = 2], in the table `({[a = 1, b = 2], [a = 3, b = 4]})`.

```powerquery-m
Table.MatchesAllRows(Table.FromRecords({[a = 1, b = 2], [a = -3, b = 4]}), each _ = [a = 1, b = 2])
```

`false`
