---
description: "Learn more about: Table.FromRecords"
title: "Table.FromRecords"
ms.date: 3/10/2022
---
# Table.FromRecords

## Syntax

<pre>
Table.FromRecords(<b>records</b> as list, optional <b>columns</b> as any, optional <b>missingField</b> as nullable number) as table
</pre>

## About

Converts `records`, a list of records, into a table.

## Example 1

Create a table from records, using record field names as column names.

**Usage**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```

## Example 2

Create a table from records with typed columns and select the number columns.

**Usage**

```powerquery-m
Table.ColumnsOfType(
    Table.FromRecords(
        {[CustomerID = 1, Name = "Bob"]},
        type table[CustomerID = Number.Type, Name = Text.Type]
    ),
    {type number}
)
```

**Output**

`{"CustomerID"}`
