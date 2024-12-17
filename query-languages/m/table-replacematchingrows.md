---
description: "Learn more about: Table.ReplaceMatchingRows"
title: "Table.ReplaceMatchingRows"
ms.subservice: m-source
---
# Table.ReplaceMatchingRows

## Syntax

<pre>
Table.ReplaceMatchingRows(<b>table</b> as table, <b>replacements</b> as list, optional <b>equationCriteria</b> as any) as table
</pre>
  
## About

Replaces all the specified rows in the `table` with the provided ones. The rows to replace and the replacements are specified in `replacements`, using {old, new} formatting. An optional `equationCriteria` parameter may be specified to control comparison between the rows of the table.

## Example 1

Replace the rows [a = 1, b = 2] and [a = 2, b = 3] with [a = -1, b = -2],[a = -2, b = -3] in the table.

**Usage**

```powerquery-m
Table.ReplaceMatchingRows(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 2, b = 3],
        [a = 3, b = 4],
        [a = 1, b = 2]
    }),
    {
        {[a = 1, b = 2], [a = -1, b = -2]},
        {[a = 2, b = 3], [a = -2, b = -3]}
    }
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = -1, b = -2],
    [a = -2, b = -3],
    [a = 3, b = 4],
    [a = -1, b = -2]
})
```

## Related content

[Equation criteria](table-functions.md#equation-criteria)
