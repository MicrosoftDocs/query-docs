---
description: "Learn more about: Table.SelectRowsWithErrors"
title: "Table.SelectRowsWithErrors | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.SelectRowsWithErrors

## Syntax

<pre>
Table.SelectRowsWithErrors(<b>table</b> as table, optional <b>columns</b> as nullable list) as table
</pre>
  
## About

Returns a table with only those rows of the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.

## Example 1

Select names of customers with errors in their rows.

**Usage**

```powerquery-m
Table.SelectRowsWithErrors(
    Table.FromRecords({
        [CustomerID = ..., Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    })
)[Name]
```

**Output**

`{"Bob"}`
