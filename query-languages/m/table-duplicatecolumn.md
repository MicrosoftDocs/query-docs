---
description: "Learn more about: Table.DuplicateColumn"
title: "Table.DuplicateColumn | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.DuplicateColumn

## Syntax

<pre>
Table.DuplicateColumn(<b>table</b> as table, <b>columnName</b> as text, <b>newColumnName</b> as text, optional <b>columnType</b> as nullable type) as table
</pre>

## About

Duplicate the column named `columnName` to the table `table`. The values and type for the column `newColumnName` are copied from column `columnName`.

## Example

Duplicate the column "a" to a column named "copied column" in the table `({[a = 1, b = 2], [a = 3, b = 4]})`.

**Usage**

```powerquery-m
Table.DuplicateColumn(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4]
    }),
    "a",
    "copied column"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = 1, b = 2, #"copied column" = 1],
    [a = 3, b = 4, #"copied column" = 3]
})
```
