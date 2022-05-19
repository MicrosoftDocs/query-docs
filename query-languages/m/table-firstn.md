---
description: "Learn more about: Table.FirstN"
title: "Table.FirstN | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.FirstN

## Syntax

<pre>
Table.FirstN(<b>table</b> as table, <b>countOrCondition</b> as any) as table
</pre>
  
## About

Returns the first row(s) of the table `table`, depending on the value of `countOrCondition`:

* If `countOrCondition` is a number, that many rows (starting at the top) will be returned.
* If `countOrCondition` is a condition, the rows that meet the condition will be returned until a row does not meet the condition.

## Example 1

Find the first two rows of the table.

**Usage**

```powerquery-m
Table.FirstN(
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
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"]
})
```

## Example 2

Find the first rows where [a] > 0 in the table.

**Usage**

```powerquery-m
Table.FirstN(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 3, b = 4],
        [a = -5, b = -6]
    }),
    each [a] > 0
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [a = 1, b = 2], 
    [a = 3, b = 4]
})
```
