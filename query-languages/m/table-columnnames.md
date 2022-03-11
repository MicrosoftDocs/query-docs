---
description: "Learn more about: Table.ColumnNames"
title: "Table.ColumnNames | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ColumnNames

## Syntax

<pre>
Table.ColumnNames(<b>table</b> as table) as list
</pre>
  
## About

Returns the column names in the table `table` as a list of text.

## Example 1

Find the column names of the table.

**Usage**

```powerquery-m
Table.ColumnNames(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    })
)
```

**Output**

`{"CustomerID", "Name", "Phone"}`
