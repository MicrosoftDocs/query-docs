---
description: "Learn more about: Table.AddColumn"
title: "Table.AddColumn | Microsoft Docs"
ms.date: 3/9/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.AddColumn

## Syntax

<pre>
Table.AddColumn(<b>table</b> as table, <b>newColumnName</b> as text, <b>columnGenerator</b> as function, optional <b>columnType</b> as nullable type) as table
</pre>
  
## About

Adds a column named `newColumnName` to the table `table`. The values for the column are computed using the specified selection function `columnGenerator` with each row taken as an input.

## Example 1

Add a column named "TotalPrice" to the table with each value being the sum of column [Price] and column [Shipping].

**Usage**

```powerquery-m
Table.AddColumn(
    Table.FromRecords({
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0, Shipping = 10.00],
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0, Shipping = 15.00],
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0, Shipping = 10.00]
    }),
    "TotalPrice",
    each [Price] + [Shipping]
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100, Shipping = 10, TotalPrice = 110],
    [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5, Shipping = 15, TotalPrice = 20],
    [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25, Shipping = 10, TotalPrice = 35]
})
```
