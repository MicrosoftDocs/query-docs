---
description: "Learn more about: Table.AlternateRows"
title: "Table.AlternateRows"
ms.subservice: m-source
---
# Table.AlternateRows

## Syntax

<pre>
Table.AlternateRows(
    <b>table</b> as table,
    <b>offset</b> as number,
    <b>skip</b> as number,
    <b>take</b> as number
) as table
</pre>
  
## About

Keeps the initial offset then alternates taking and skipping the following rows.

* `table`: The input table.
* `offset`: The number of rows to keep before starting iterations.
* `skip`: The number of rows to remove in each iteration.
* `take`: The number of rows to keep in each iteration.

## Example 1

Return a table from the table that, starting at the first row, skips 1 value and then keeps 1 value.

**Usage**

```powerquery-m
Table.AlternateRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    }),
    1,
    1,
    1
)
```

**Output**

```powerquery-m
Table.FromRecords({
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
})
```
