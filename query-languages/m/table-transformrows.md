---
description: "Learn more about: Table.TransformRows"
title: "Table.TransformRows"
ms.subservice: m-source
---
# Table.TransformRows

## Syntax

<pre>
Table.TransformRows(<b>table</b> as table, <b>transform</b> as function) as list
</pre>

## About

Creates a `list` by applying the `transform` operation to each row in `table`.

## Example 1  

Transform the rows of a table into a list of numbers.

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

Transform the rows of a numeric table into textual records.

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
