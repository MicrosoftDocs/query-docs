---
description: "Learn more about: Table.ToRecords"
title: "Table.ToRecords | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Table.ToRecords

## Syntax

<pre>
Table.ToRecords(<b>table</b> as table) as list  
</pre>
  
## About

Converts a table, `table`, to a list of records.

## Example 1
  
Convert the table to a list of records.

**Usage**

```powerquery-m
Table.ToRecords(
    Table.FromRows(
        {
            {1, "Bob", "123-4567"},
            {2, "Jim", "987-6543"},
            {3, "Paul", "543-7890"}
        },
        {"CustomerID", "Name", "Phone"}
    )
)
```

**Output**

```powerquery-m
{
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
}
```
