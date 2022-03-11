---
description: "Learn more about: Table.Group"
title: "Table.Group | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.Group

## Syntax

<pre>
Table.Group(<b>table</b> as table, <b>key</b> as any, <b>aggregatedColumns</b> as list, optional <b>groupKind</b> as nullable number, optional <b>comparer</b> as nullable function) as table
</pre>
  
## About

Groups the rows of `table` by the key columns defined by `key`. The `key` can either be a single column name, or a list of column names. For each group, a record is constructed containing the key columns (and their values), along with any aggregated columns specified by `aggregatedColumns`. Optionally, `groupKind` and `comparer` may also be specified.

If the data is already sorted by the key columns, then a `groupKind` of GroupKind.Local can be provided. This may improve the performance of grouping in certain cases, since all the rows with a given set of key values are assumed to be contiguous.

When passing a `comparer`, note that if it treats differing keys as equal, a row may be placed in a group whose keys differ from its own.

This function does not guarantee the ordering of the rows it returns.

## Example 1

Group the table adding an aggregate column [total] which contains the sum of prices ("each List.Sum([price])").

**Usage**

```powerquery-m
Table.Group(
    Table.FromRecords({
        [CustomerID = 1, price = 20],
        [CustomerID = 2, price = 10],
        [CustomerID = 2, price = 20],
        [CustomerID = 1, price = 10],
        [CustomerID = 3, price = 20],
        [CustomerID = 3, price = 5]
    }),
    "CustomerID",
    {"total", each List.Sum([price])}
)
```

**Output**

```powerquery-m
Table.FromRecords(
    {
        [CustomerID = 1, total = 30],
        [CustomerID = 2, total = 30],
        [CustomerID = 3, total = 25]
    },
    {"CustomerID", "total"}
)
```
