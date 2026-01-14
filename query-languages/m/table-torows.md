---
description: "Learn more about: Table.ToRows"
title: "Table.ToRows"
ms.subservice: m-source
ms.topic: reference
---
# Table.ToRows

## Syntax

<pre>
Table.ToRows(<b>table</b> as table) as list
</pre>
  
## About

Creates a list of nested lists from the table, `table`. Each list item is an inner list that contains the row values.  

## Example 1

Create a list of the row values from the table.

**Usage**

```powerquery-m
Table.ToRows(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"]
    })
)
```

**Output**

```powerquery-m
{
    {1, "Bob", "123-4567"},
    {2, "Jim", "987-6543"},
    {3, "Paul", "543-7890"}
}
```
