---
description: "Learn more about: Table.InsertRows"
title: "Table.InsertRows | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.InsertRows

## Syntax

<pre>
Table.InsertRows(<b>table</b> as table, <b>offset</b> as number, <b>rows</b> as list) as table
</pre>
  
## About

Returns a table with the list of rows, `rows`, inserted into the `table` at the given position, `offset`. Each column in the row to insert much match the column types of the table.

## Example 1

Insert the row into the table at position 1.

**Usage**

```powerquery-m
Table.InsertRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"]
    }),
    1,
    {[CustomerID = 3, Name = "Paul", Phone = "543-7890"]}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"]
})
```

## Example 2

Insert two rows into the table at position 1.

**Usage**

```powerquery-m
Table.InsertRows(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    1,
    {
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    }
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```
