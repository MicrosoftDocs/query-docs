---
description: "Learn more about: Table.ReplaceRows"
title: "Table.ReplaceRows | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ReplaceRows

## Syntax

<pre>
Table.ReplaceRows(<b>table</b> as table, <b>offset</b> as number, <b>count</b> as number, <b>rows</b> as list) as table
</pre>
  
## About

Replaces a specified number of rows, `count`, in the input `table` with the specified `rows`, beginning after the `offset`. The `rows` parameter is a list of records. 

* `table`: The table where the replacement is performed.
* `offset`: The number of rows to skip before making the replacement.
* `count`: The number of rows to replace.
* `rows`: The list of row records to insert into the `table` at the location specified by the `offset`.

## Example 1

Starting at position 1, replace 3 rows.

**Usage**

```powerquery-m
Table.ReplaceRows(
    Table.FromRecords({
        [Column1 = 1],
        [Column1 = 2],
        [Column1 = 3],
        [Column1 = 4],
        [Column1 = 5]
    }),
    1,
    3,
    {[Column1 = 6], [Column1 = 7]}
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [Column1 = 1],
    [Column1 = 6],
    [Column1 = 7],
    [Column1 = 5]
})
```
