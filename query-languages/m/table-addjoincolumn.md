---
description: "Learn more about: Table.AddJoinColumn"
title: "Table.AddJoinColumn"
---
# Table.AddJoinColumn

## Syntax

<pre>
Table.AddJoinColumn(table1 as table, key1 as any, table2 as function, key2 as any, newColumnName as text) as table
</pre>

## About

Joins the rows of `table1` with the rows of `table2` based on the equality of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`). The results are entered into the column named `newColumnName`. This function behaves similarly to [Table.Join](/powerquery-m/table-join) with a JoinKind of LeftOuter except that the join results are presented in a nested rather than flattened fashion.

## Example 1

Add a join column to ({[saleID = 1, item = "Shirt"], [saleID = 2, item = "Hat"]}) named "price/stock" from the table ({[saleID = 1, price = 20], [saleID = 2, price = 10]}) joined on [saleID].

**Usage**

```powerquery-m
Table.AddJoinColumn(
    Table.FromRecords({
        [saleID = 1, item = "Shirt"],
        [saleID = 2, item = "Hat"]
    }),
    "saleID",
    () => Table.FromRecords({
        [saleID = 1, price = 20, stock = 1234],
        [saleID = 2, price = 10, stock = 5643]
    }),
    "saleID",
    "price"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [
        saleID = 1,
        item = "Shirt",
        price = Table.FromRecords({[saleID = 1, price = 20, stock = 1234]})
    ],
    [
        saleID = 2,
        item = "Hat",
        price = Table.FromRecords({[saleID = 2, price = 10, stock = 5643]})
    ]
})
```
