---
description: "Learn more about: Table.ExpandListColumn"
title: "Table.ExpandListColumn | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ExpandListColumn

## Syntax

<pre>
Table.ExpandListColumn(<b>table</b> as table, <b>column</b> as text) as table
</pre>
  
## About

Given a `table`, where a `column` is a list of values, splits the list into a row for each value. Values in the other columns are duplicated in each new row created.

## Example 1

Split the list column [Name] in the table.

**Usage**

```powerquery-m
Table.ExpandListColumn(
    Table.FromRecords({[Name = {"Bob", "Jim", "Paul"}, Discount = .15]}),
    "Name"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Name = "Bob", Discount = 0.15],
    [Name = "Jim", Discount = 0.15],
    [Name = "Paul", Discount = 0.15]
})
```
