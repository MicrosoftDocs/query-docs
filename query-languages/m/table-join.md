---
description: "Learn more about: Table.Join"
title: "Table.Join | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.Join

## Syntax

<pre>
Table.Join(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as table, <b>key2</b> as any, optional <b>joinKind</b> as nullable number, optional <b>joinAlgorithm</b> as nullable number, optional <b>keyEqualityComparers</b> as nullable list) as table
</pre>

## About

Joins the rows of `table1` with the rows of `table2` based on the equality of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`).

By default, an inner join is performed, however an optional `joinKind` may be included to specify the type of join. Options include:

* `JoinKind.Inner`
* `JoinKind.LeftOuter`
* `JoinKind.RightOuter`
* `JoinKind.FullOuter`
* `JoinKind.LeftAnti`
* `JoinKind.RightAnti`

An optional set of `keyEqualityComparers` may be included to specify how to compare the key columns. This feature is currently intended for internal use only.

## Example 1

Join two tables using a single key column.

**Usage**

```powerquery-m
Table.Join(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "CustomerID",
    Table.FromRecords({
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0],
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0],
        [OrderID = 4, CustomerID = 3, Item = "Fish tazer", Price = 200.0],
        [OrderID = 5, CustomerID = 3, Item = "Bandaids", Price = 2.0],
        [OrderID = 6, CustomerID = 1, Item = "Tackle box", Price = 20.0],
        [OrderID = 7, CustomerID = 5, Item = "Bait", Price = 3.25]
    }),
    "CustomerID"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567", OrderID = 1, Item = "Fishing rod", Price = 100],
    [CustomerID = 1, Name = "Bob", Phone = "123-4567", OrderID = 2, Item = "1 lb. worms", Price = 5],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543", OrderID = 3, Item = "Fishing net", Price = 25],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890", OrderID = 4, Item = "Fish tazer", Price = 200],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890", OrderID = 5, Item = "Bandaids", Price = 2],
    [CustomerID = 1, Name = "Bob", Phone = "123-4567", OrderID = 6, Item = "Tackle box", Price = 20]
})
```
