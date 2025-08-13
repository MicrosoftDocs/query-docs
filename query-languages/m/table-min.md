---
description: "Learn more about: Table.Min"
title: "Table.Min"
ms.subservice: m-source
---
# Table.Min

## Syntax

<pre>
Table.Min(
    <b>table</b> as table,
    <b>comparisonCriteria</b> as any,
    optional <b>default</b> as any
) as any
</pre>
  
## About

Returns the smallest row in the `table`, given the `comparisonCriteria`. If the table is empty, the optional `default` value is returned.

## Example 1

Find the row with the smallest value in column [a] in the table.

**Usage**

```powerquery-m
Table.Min(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 6, b = 8]
    }),
    "a"
)
```

**Output**

`[a = 2, b = 4]`

## Example 2

Find the row with the smallest value in column [a] in the table. Return -1 if empty.

**Usage**

```powerquery-m
Table.Min(#table({"a"}, {}), "a", -1)
```

**Output**

`-1`

## Related content

[Comparison criteria](table-functions.md#comparison-criteria)
