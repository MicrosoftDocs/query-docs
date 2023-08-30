---
description: "Learn more about: Table.RowCount"
title: "Table.RowCount"
---
# Table.RowCount

## Syntax

<pre>
Table.RowCount(<b>table</b> as table) as number
</pre>
  
## About

Returns the number of rows in the `table`.

## Example 1

Find the number of rows in the table.

**Usage**

```powerquery-m
Table.RowCount(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

**Output**

`3`
