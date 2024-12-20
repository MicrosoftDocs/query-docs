---
description: "Learn more about: Table.MatchesAnyRows"
title: "Table.MatchesAnyRows"
ms.subservice: m-source
---
# Table.MatchesAnyRows

## Syntax

<pre>
Table.MatchesAnyRows(<b>table</b> as table, <b>condition</b> as function) as logical 
</pre>
  
## About

Indicates whether any the rows in the `table` match the given `condition`. Returns `true` if any of the rows match, `false` otherwise.

## Example 1

Determine whether any of the row values in column [a] are even in the table `({[a = 2, b = 4], [a = 6, b = 8]})`.

**Usage**

```powerquery-m
Table.MatchesAnyRows(
    Table.FromRecords({
        [a = 1, b = 4],
        [a = 3, b = 8]
    }),
    each Number.Mod([a], 2) = 0
)
```

**Output**

`false`

## Example 2

Determine whether any of the row values are [a = 1, b = 2], in the table `({[a = 1, b = 2], [a = 3, b = 4]})`.

**Usage**

```powerquery-m
Table.MatchesAnyRows(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = -3, b = 4]
    }),
    each _ = [a = 1, b = 2]
)
```

**Output**

`true`
