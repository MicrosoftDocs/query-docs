---
description: "Learn more about: Table.RemoveFirstN"
title: "Table.RemoveFirstN | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo
---
# Table.RemoveFirstN
  
## Syntax

<pre>
Table.RemoveFirstN(<b>table</b> as table, optional <b>countOrCondition</b> as any) as table
</pre>
  
## About

Returns a table that does not contain the first specified number of rows, `countOrCondition`, of the table `table`. The number of rows removed depends on the optional parameter `countOrCondition`.

* If `countOrCondition` is omitted only the first row is removed.
* If `countOrCondition` is a number, that many rows (starting at the top) will be removed.
* If `countOrCondition` is a condition, the rows that meet the condition will be removed until a row does not meet the condition.

## Example 1

Remove the first row of the table.

**Usage**

```powerquery-m
Table.RemoveFirstN(
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
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```

## Example 2

Remove the first two rows of the table.

**Usage**

```powerquery-m
Table.RemoveFirstN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    2
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```

## Example 3

Remove the first rows where [CustomerID] <=2 of the table.

**Usage**

```powerquery-m
Table.RemoveFirstN(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"], 
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"] , 
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"] , 
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }), 
    each [CustomerID] <= 2
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
})
```
