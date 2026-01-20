---
description: "Learn more about: Table.MaxN"
title: "Table.MaxN"
ms.subservice: m-source
ms.topic: reference
---
# Table.MaxN

## Syntax

<pre>
Table.MaxN(
    <b>table</b> as table,
    <b>comparisonCriteria</b> as any,
    <b>countOrCondition</b> as any
) as table
</pre>
  
## About

Returns the largest row(s) in the `table`, given the `comparisonCriteria`. After the rows are sorted, the `countOrCondition` parameter must be specified to further filter the result. Note the sorting algorithm cannot guarantee a fixed sorted result. The `countOrCondition` parameter can take multiple forms:

* If a number is specified, a list of up to `countOrCondition` items in ascending order is returned.
* If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.

## Example 1

Find the row with the largest value in column [a] with the condition [a] > 0, in the table. The rows are sorted before the filter is applied.

**Usage**

```powerquery-m
Table.MaxN(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 0, b = 0],
        [a = 6, b = 2]
    }),
    "a",
    each [a] > 0
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = 6, b = 2],
    [a = 2, b = 4]
})
```

## Example 2

Find the row with the largest value in column [a] with the condition [b] > 0, in the table. The rows are sorted before the filter is applied.

**Usage**

```powerquery-m
Table.MaxN(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 8, b = 0],
        [a = 6, b = 2]
    }),
    "a",
    each [b] > 0
)
```

**Output**

`Table.FromRecords({})`

## Related content

[Comparison criteria](table-functions.md#comparison-criteria)
