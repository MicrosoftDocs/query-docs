---
description: "Learn more about: Table.RemoveLastN"
title: "Table.RemoveLastN | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.RemoveLastN

## Syntax

<pre>
Table.RemoveLastN(<b>table</b> as table, optional <b>countOrCondition</b> as any) as table
</pre>
  
## About

Returns a table that does not contain the last `countOrCondition` rows of the table `table`. The number of rows removed depends on the optional parameter `countOrCondition`.

* If `countOrCondition` is omitted only the last row is removed.
* If `countOrCondition` is a number, that many rows (starting at the bottom) will be removed.
* If `countOrCondition` is a condition, the rows that meet the condition will be removed until a row does not meet the condition.

## Example 1

Remove the last row of the table.

**Usage**

```powerquery-m
Table.RemoveLastN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    1
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```

## Example 2

Remove the last rows where [CustomerID] > 2 of the table.

**Usage**

```powerquery-m
Table.RemoveLastN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    each [CustomerID] >= 2
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`
