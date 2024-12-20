---
description: "Learn more about: Table.SingleRow"
title: "Table.SingleRow"
ms.subservice: m-source
---
# Table.SingleRow

## Syntax

<pre>
Table.SingleRow(<b>table</b> as table) as record  
</pre>
  
## About

Returns the single row in the one row `table`. If the `table` does not contain exactly one row, an error is raised.

## Example 1

Return the single row in the table.

**Usage**

```powerquery-m
Table.SingleRow(Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}))
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`
