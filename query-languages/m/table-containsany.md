---
description: "Learn more about: Table.ContainsAny"
title: "Table.ContainsAny"
ms.date: 3/14/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ContainsAny

## Syntax

<pre>
Table.ContainsAny(<b>table</b> as table, <b>rows</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>
  
## About

Indicates whether any the specified records in the list of records `rows`, appear as rows in the `table`. An optional parameter `equationCriteria` may be specified to control comparison between the rows of the table.

## Example 1

Determine if the table `({[a = 1, b = 2], [a = 3, b = 4]})` contains the rows `[a = 1, b = 2]` or `[a = 3, b = 5]`.

**Usage**

```powerquery-m
Table.ContainsAny(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4]
    }),
    {
        [a = 1, b = 2],
        [a = 3, b = 5]
    }
)
```

**Output**

`true`

## Example 2

Determine if the table `({[a = 1, b = 2], [a = 3, b = 4]})` contains the rows `[a = 1, b = 3]` or `[a = 3, b = 5]`.

**Usage**

```powerquery-m
Table.ContainsAny(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4]
    }),
    {
        [a = 1, b = 3],
        [a = 3, b = 5]
    }
)
```

**Output**

`false`

## Example 3

Determine if the table `(Table.FromRecords({[a = 1, b = 2], [a = 3, b = 4]}))` contains the rows `[a = 1, b = 3]` or `[a = 3, b = 5]` comparing only the column [a].

**Usage**

```powerquery-m
Table.ContainsAny(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4]
    }),
    {
        [a = 1, b = 3],
        [a = 3, b = 5]
    },
    "a"
)
```

**Output**

`true`
