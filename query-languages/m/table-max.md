---
description: "Learn more about: Table.Max"
title: "Table.Max"
ms.subservice: m-source
ms.topic: reference
---
# Table.Max

## Syntax

<pre> 
Table.Max(
    <b>table</b> as table,
    <b>comparisonCriteria</b> as any,
    optional <b>default</b> as any
) as any
</pre>
  
## About

Returns the largest row in the `table`, given the `comparisonCriteria`. If the table is empty, the optional `default` value is returned.

## Example 1

Find the row with the largest value in column [a] in the table `({[a = 2, b = 4], [a = 6, b = 8]})`.

**Usage**

```powerquery-m
Table.Max(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 6, b = 8]
    }),
    "a"
)
```

**Output**

`[a = 6, b = 8]`

## Example 2

Find the row with the largest value in column [a] in the table `({})`. Return -1 if empty.

**Usage**

```powerquery-m
Table.Max(#table({"a"}, {}), "a", -1)
```

**Output**

`-1`

## Related content

[Comparison criteria](table-functions.md#comparison-criteria)
