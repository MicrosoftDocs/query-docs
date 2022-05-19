---
description: "Learn more about: Table.FillUp"
title: "Table.FillUp | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.FillUp

## Syntax

<pre>
Table.FillUp(<b>table</b> as table, <b>columns</b> as list) as table
</pre>

## About

Returns a table from the `table` specified where the value of the next cell is propagated to the null-valued cells above in the `columns` specified.

## Example 1

Return a table with the null values in column [Column2] filled with the value below them from the table.

**Usage**

```powerquery-m
Table.FillUp(
    Table.FromRecords({
        [Column1 = 1, Column2 = 2],
        [Column1 = 3, Column2 = null],
        [Column1 = 5, Column2 = 3]
    }),
    {"Column2"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = 1, Column2 = 2],
    [Column1 = 3, Column2 = 3],
    [Column1 = 5, Column2 = 3]
})
```
