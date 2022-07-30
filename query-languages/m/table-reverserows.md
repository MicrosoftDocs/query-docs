---
description: "Learn more about: Table.ReverseRows"
title: "Table.ReverseRows | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ReverseRows

## Syntax

<pre>
Table.ReverseRows(<b>table</b> as table) as table
</pre>

## About

Returns a table with the rows from the input `table` in reverse order.

## Example 1

Reverse the rows in the table.

**Usage**

```powerquery-m
Table.ReverseRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    })
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"]
})
```
