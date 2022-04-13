---
description: "Learn more about: Table.TransformRows"
title: "Table.TransformRows | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.TransformRows

## Syntax

<pre>
Table.TransformRows(<b>table</b> as table, <b>transform</b> as function) as list
</pre>

## About

Creates a `list` by applying the `transform` operation to each row in `table`.

## Example 1  

Transform the rows into a list of numbers from the table `({[A = 1], [A = 2], [A = 3], [A = 4], [A = 5]})`.

**Usage**

```powerquery-m
Table.TransformRows(
    Table.FromRecords({
        [a = 1],
        [a = 2],
        [a = 3],
        [a = 4],
        [a = 5]
    }),
    each [a]
)
```

**Output**

`{1, 2, 3, 4, 5}`

## Example 2

Transform the rows in column [A] into text values in a column [B] from the table `({[A = 1], [A = 2], [A = 3], [A = 4], [A = 5])`.

**Usage**

```powerquery-m
Table.TransformRows(
    Table.FromRecords({
        [a = 1],
        [a = 2],
        [a = 3],
        [a = 4],
        [a = 5]
    }),
    (row) as record => [B = Number.ToText(row[a])]
)
```

**Output**

```powerquery-m
{
    [B = "1"],
    [B = "2"],
    [B = "3"],
    [B = "4"],
    [B = "5"]
}
```
