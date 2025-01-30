---
description: "Learn more about: Table.SplitAt"
title: "Table.SplitAt"
ms.subservice: m-source
---
# Table.SplitAt

<pre>
Table.SplitAt(<b>table</b> as table, <b>count</b> as number) as list
</pre>

## About

Returns a list containing two tables: a table with the first N rows of `table` (as specified by `count`) and a table containing the remaining rows of `table`. If the tables of the resulting list are enumerated exactly once and in order, the function will enumerate `table` only once.

## Example 1

Return the first two rows of the table and the remaining rows of the table.

**Usage**

```powerquery-m
Table.SplitAt(#table({"a", "b", "c"}, {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}), 2)
```

**Output**

```powerquery-m
{
    #table({"a", "b", "c"}, {{1, 2, 3}, {4, 5, 6}}),
    #table({"a", "b", "c"}, {{7, 8, 9}})
}
```
