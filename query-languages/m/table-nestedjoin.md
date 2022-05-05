---
description: "Learn more about: Table.NestedJoin"
title: "Table.NestedJoin | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.NestedJoin

## Syntax

<pre>
Table.NestedJoin(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as any, <b>key2</b> as any, <b>newColumnName</b> as text, optional <b>joinKind</b> as nullable number, optional <b>keyEqualityComparers</b> as nullable list) as table
</pre>

## About

Joins the rows of `table1` with the rows of `table2` based on the equality of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`). The results are entered into the column named `newColumnName`.

The optional `joinKind` specifies the kind of join to perform. By default, a left outer join is performed if a `joinKind` is not specified.

An optional set of `keyEqualityComparers` may be included to specify how to compare the key columns. This `keyEqualityComparers` feature is currently intended for internal use only.

## Example 1

Join two tables using a single key column.

**Usage**

```powerquery-m
Table.NestedJoin(
    Table.FromRecords({
        [CustomerToCall = 1],
        [CustomerToCall = 3]
    }),
    {"CustomerToCall"},
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    {"CustomerID"},
    "CustomerDetails"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerToCall = 1, CustomerDetails = Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})],
    [CustomerToCall = 3, CustomerDetails = Table.FromRecords({[CustomerID = 3, Name = "Paul", Phone = "543-7890"]})]
})
```
