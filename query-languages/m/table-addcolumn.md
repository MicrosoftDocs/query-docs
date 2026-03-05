---
description: "Learn more about: Table.AddColumn"
title: "Table.AddColumn"
ms.subservice: m-source
ms.topic: reference
---
# Table.AddColumn

## Syntax

<pre>
Table.AddColumn(
    <b>table</b> as table,
    <b>newColumnName</b> as text,
    <b>columnGenerator</b> as function,
    optional <b>columnType</b> as nullable type
) as table
</pre>
  
## About

Adds a column named `newColumnName` to the table `table`. The values for the column are computed using the specified selection function `columnGenerator` with each row taken as an input.

## Example 1

Add a number column named "TotalPrice" to the table, with each value being the sum of the [Price] and [Shipping] columns.

**Usage**

```powerquery-m
Table.AddColumn(
    Table.FromRecords({
        [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0, Shipping = 10.00],
        [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0, Shipping = 15.00],
        [OrderID = 3, CustomerID = 2, Item = "Fishing net", Price = 25.0, Shipping = 10.00]
    }),
    "TotalPrice",
    each [Price] + [Shipping],
    type number
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

## Related content

* [Types and type conversion](type-conversion.md)
