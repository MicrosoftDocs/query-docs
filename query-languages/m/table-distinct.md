---
description: "Learn more about: Table.Distinct"
title: "Table.Distinct"
ms.date: 3/10/2022
---
# Table.Distinct

## Syntax

<pre>
Table.Distinct(<b>table</b> as table, optional <b>equationCriteria</b> as any) as table
</pre>
  
## About

Removes duplicate rows from the table `table`. An optional parameter, `equationCriteria`, specifies which columns of the table are tested for duplication. If `equationCriteria` is not specified, all columns are tested.

## Example 1

Remove the duplicate rows from the table.

**Usage**

```powerquery-m
Table.Distinct(
    Table.FromRecords({
        [a = "A", b = "a"],
        [a = "B", b = "b"],
        [a = "A", b = "a"]
    })
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = "A", b = "a"],
    [a = "B", b = "b"]
})
```

## Example 2

Remove the duplicate rows from column [b] in the table `({[a = "A", b = "a"], [a = "B", b = "a"], [a = "A", b = "b"]})`.

**Usage**

```powerquery-m
Table.Distinct(
    Table.FromRecords({
        [a = "A", b = "a"],
        [a = "B", b = "a"],
        [a = "A", b = "b"]
    }),
    "b"
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = "A", b = "a"],
    [a = "A", b = "b"]
})
```
