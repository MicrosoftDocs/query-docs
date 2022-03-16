---
description: "Learn more about: Table.ExpandTableColumn"
title: "Table.ExpandTableColumn | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ExpandTableColumn

## Syntax

<pre>
Table.ExpandTableColumn(<b>table</b> as table, <b>column</b> as text, <b>columnNames</b> as list, optional <b>newColumnNames</b> as nullable list) as table
</pre>
  
## About

Expands tables in `table`[`column`] into multiple rows and columns. `columnNames` is used to select the columns to expand from the inner table. Specify `newColumnNames` to avoid conflicts between existing columns and new columns.

## Example 1

Expand table columns in `[a]` in the table `({[t = {[a=1, b=2, c=3], [a=2,b=4,c=6]}, b = 2]})` into 3 columns `[t.a]`, `[t.b]` and `[t.c]`.

**Usage**

```powerquery-m
Table.ExpandTableColumn(
    Table.FromRecords({
        [
            t = Table.FromRecords({
                [a = 1, b = 2, c = 3],
                [a = 2, b = 4, c = 6]
            }),
            b = 2
        ]
    }),
    "t",
    {"a", "b", "c"},
    {"t.a", "t.b", "t.c"}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [t.a = 1, t.b = 2, t.c = 3, b = 2],
    [t.a = 2, t.b = 4, t.c = 6, b = 2]
})
```
