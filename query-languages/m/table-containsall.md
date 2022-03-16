---
description: "Learn more about: Table.ContainsAll"
title: "Table.ContainsAll | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ContainsAll

## Syntax

<pre>
Table.ContainsAll(<b>table</b> as table, <b>rows</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>
  
## About

Indicates whether all the specified records in the list of records `rows`, appear as rows in the `table`. An optional parameter `equationCriteria` may be specified to control comparison between the rows of the table.

## Example 1

Determine if the table contains all the rows, comparing only the column [CustomerID].

**Usage**

```powerquery-m
Table.ContainsAll(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    {
        [CustomerID = 1, Name = "Bill"],
        [CustomerID = 2, Name = "Fred"]
    },
    "CustomerID"
)
```

**Output**

`true`

## Example 2

Determine if the table contains all the rows.

**Usage**

```powerquery-m
Table.ContainsAll(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    {
        [CustomerID = 1, Name = "Bill"],
        [CustomerID = 2, Name = "Fred"]
    }
)
```

**Output**

`false`
