---
description: "Learn more about: Table.Distinct"
title: "Table.Distinct"
ms.date: 9/15/2022
---
# Table.Distinct

## Syntax

<pre>
Table.Distinct(<b>table</b> as table, optional <b>equationCriteria</b> as any) as table
</pre>
  
## About

Removes duplicate rows from the table. An optional parameter, `equationCriteria`, specifies which columns of the table are tested for duplication. If `equationCriteria` is not specified, all columns are tested.

Because Power Query sometimes offloads certain operations to backend data sources (known as *folding*), and also sometimes optimizes queries by skipping operations that aren't strictly necessary, in general there's no guarantee which specific duplicate will be preserved. For example, you can't assume that the first row with a unique set of column values will remain, and rows further down in the table will be removed. If you want the duplicate removal to behave predictably, first buffer the table using [Table.Buffer](table-buffer.md).

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
