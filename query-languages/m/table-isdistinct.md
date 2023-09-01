---
description: "Learn more about: Table.IsDistinct"
title: "Table.IsDistinct"
---
# Table.IsDistinct

## Syntax

<pre>
Table.IsDistinct(<b>table</b> as table, optional <b>comparisonCriteria</b> as any) as logical  
</pre>
  
## About

Indicates whether the `table` contains only distinct rows (no duplicates). Returns `true` if the rows are distinct, `false` otherwise. An optional parameter, `comparisonCriteria`, specifies which columns of the table are tested for duplication. If `comparisonCriteria` is not specified, all columns are tested.

## Example 1

Determine if the table is distinct.

**Usage**

```powerquery-m
Table.IsDistinct(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    })
)
```

**Output**

`true`

## Example 2

Determine if the table is distinct in column.

**Usage**

```powerquery-m
Table.IsDistinct(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 5, Name = "Bob", Phone = "232-1550"]
    }),
    "Name"
)
```

**Output**

`false`
