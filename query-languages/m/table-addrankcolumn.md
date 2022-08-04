---
description: "Learn more about: Table.AddRankColumn"
title: "Table.AddRankColumn"
ms.date: 5/19/2022
---
# Table.AddRankColumn

## Syntax

<pre>
Table.AddRankColumn(<b>table</b> as table, <b>newColumnName</b> as text, <b>comparisonCriteria</b> as any, optional <b>options</b> as nullable record) as table
</pre>
  
## About

Appends a column named `newColumnName` to the `table` with the ranking of one or more other columns described by `comparisonCriteria`. The `RankKind` option in `options` can be used by advanced users to pick a more-specific ranking method.

## Example 1

Add a column named **RevenueRank** to the table which ranks the **Revenue** column from highest to lowest.

**Usage**

```powerquery-m
Table.AddRankColumn(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Revenue = 200],
        [CustomerID = 2, Name = "Jim", Revenue = 100],
        [CustomerID = 3, Name = "Paul", Revenue = 200],
        [CustomerID = 4, Name = "Ringo", Revenue = 50]
    }),
    "RevenueRank",
    {"Revenue", Order.Descending},
    [RankKind = RankKind.Competition]
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Revenue = 200, RevenueRank = 1],
    [CustomerID = 3, Name = "Paul", Revenue = 200, RevenueRank = 1],
    [CustomerID = 2, Name = "Jim", Revenue = 100, RevenueRank = 3],
    [CustomerID = 4, Name = "Ringo", Revenue = 50, RevenueRank = 4]
})
```
