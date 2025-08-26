---
description: "Learn more about: Table.PositionOfAny"
title: "Table.PositionOfAny"
ms.subservice: m-source
---
# Table.PositionOfAny

## Syntax

<pre> 
Table.PositionOfAny(
    <b>table</b> as table,
    <b>rows</b> as list,
    optional <b>occurrence</b> as nullable number,
    optional <b>equationCriteria</b> as any
) as any
</pre>
  
## About

Returns the row(s) position(s) from the `table` of the first occurrence of the list of `rows`. Returns -1 if no occurrence is found.

* `table`: The input table.
* `rows`: The list of rows in the table to find the positions of.
* `occurrence`: _[Optional]_ Specifies which occurrences of the row to return.
* `equationCriteria: _[Optional]_ Controls the comparison between the table rows.

## Example 1

Find the position of the first occurrence of [a = 2, b = 4] or [a = 6, b = 8] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

**Usage**

```powerquery-m
Table.PositionOfAny(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 1, b = 4],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    {
        [a = 2, b = 4],
        [a = 6, b = 8]
    }
)
```

**Output**

`0`

## Example 2

Find the position of all the occurrences of [a = 2, b = 4] or [a = 6, b = 8] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}`.

**Usage**

```powerquery-m
Table.PositionOfAny(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 6, b = 8],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    {
        [a = 2, b = 4],
        [a = 6, b = 8]
    },
    Occurrence.All
)
```

**Output**

`{0, 1, 2}`

## Related content

[Equation criteria](table-functions.md#equation-criteria)
