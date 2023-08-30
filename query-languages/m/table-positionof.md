---
description: "Learn more about: Table.PositionOf"
title: "Table.PositionOf"
---
# Table.PositionOf

## Syntax

<pre>
Table.PositionOf(<b>table</b> as table, <b>row</b> as record, optional <b>occurrence</b> as any, optional <b>equationCriteria</b> as any) as any
</pre>
  
## About

Returns the row position of the first occurrence of the `row` in the `table` specified. Returns -1 if no occurrence is found.

* `table`: The input table.
* `row`: The row in the table to find the position of.
* `occurrence`: _[Optional]_ Specifies which occurrences of the row to return.
* `equationCriteria`: _[Optional]_ Controls the comparison between the table rows.

## Example 1

Find the position of the first occurrence of [a = 2, b = 4] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

**Usage**

```powerquery-m
Table.PositionOf(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 1, b = 4],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    [a = 2, b = 4]
)
```

**Output**

`0`

## Example 2

Find the position of the second occurrence of [a = 2, b = 4] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

**Usage**

```powerquery-m
Table.PositionOf(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 1, b = 4],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    [a = 2, b = 4],
    1
)
```

**Output**

`2`

## Example 3

Find the position of all the occurrences of [a = 2, b = 4] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

**Usage**

```powerquery-m
Table.PositionOf(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 1, b = 4],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    [a = 2, b = 4],
    Occurrence.All
)
```

**Output**

`{0, 2}`
