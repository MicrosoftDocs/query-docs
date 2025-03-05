---
description: "Learn more about: Table.ToColumns"
title: "Table.ToColumns"
ms.subservice: m-source
---
# Table.ToColumns

## Syntax

<pre>
Table.ToColumns(<b>table</b> as table) as list
</pre>
  
## About

Creates a list of nested lists from the table, `table`. Each list item is an inner list that contains the column values.  
  
## Example 1

Create a list of the column values from the table.

**Usage**

```powerquery-m
Table.ToColumns(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"]
    })
) 
```

**Output**

`{{1, 2}, {"Bob", "Jim"}, {"123-4567", "987-6543"}}`
