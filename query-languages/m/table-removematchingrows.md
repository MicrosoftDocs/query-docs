---
description: "Learn more about: Table.RemoveMatchingRows"
title: "Table.RemoveMatchingRows"
ms.date: 3/10/2022
---
# Table.RemoveMatchingRows

## Syntax

<pre>
Table.RemoveMatchingRows(<b>table</b> as table, <b>rows</b> as list, optional <b>equationCriteria</b> as any) as table
</pre>
  
## About

Removes all occurrences of the specified `rows` from the `table`. An optional parameter `equationCriteria` may be specified to control the comparison between the rows of the table.

## Example 1

Remove any rows where [a = 1] from the table `({[a = 1, b = 2], [a = 3, b = 4], [a = 1, b = 6]})`.

**Usage**

```powerquery-m
Table.RemoveMatchingRows(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4],
        [a = 1, b = 6]
    }),
    {[a = 1]},
    "a"
)
```

**Output**

`Table.FromRecords({[a = 3, b = 4]})`
