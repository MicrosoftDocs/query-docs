---
description: "Learn more about: Table.ColumnCount"
title: "Table.ColumnCount"
ms.subservice: m-source
---
# Table.ColumnCount

## Syntax

<pre>
Table.ColumnCount(<b>table</b> as table) as number
</pre>
  
## About

Returns the number of columns in the table `table`.

## Example 1

Find the number of columns in the table.

**Usage**

```powerquery-m
Table.ColumnCount(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

**Output**

`3`
