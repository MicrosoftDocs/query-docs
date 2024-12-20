---
description: "Learn more about: Table.LastN"
title: "Table.LastN"
ms.subservice: m-source
---
# Table.LastN

## Syntax

<pre>
Table.LastN(<b>table</b> as table, <b>countOrCondition</b> as any) as table
</pre>
  
## About

Returns the last row(s) from the table, `table`, depending on the value of `countOrCondition`:

* If `countOrCondition` is a number, that many rows will be returned starting from position (end - `countOrCondition`).
* If `countOrCondition` is a condition, the rows that meet the condition will be returned in ascending position until a row does not meet the condition.

## Example 1

Find the last two rows of the table.

**Usage**

```powerquery-m
Table.LastN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    }),
    2
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```

## Example 2

Find the last rows where [a] > 0 in the table.

**Usage**

```powerquery-m
Table.LastN(
    Table.FromRecords({
        [a = -1, b = -2],
        [a = 3, b = 4],
        [a = 5, b = 6]
    }),
    each _ [a] > 0

```

**Output**

```powerquery-m
Table.FromRecords({
    [a = 3, b = 4],
    [a = 5, b = 6]
})
```
