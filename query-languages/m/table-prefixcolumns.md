---
description: "Learn more about: Table.PrefixColumns"
title: "Table.PrefixColumns"
ms.subservice: m-source
---
# Table.PrefixColumns

## Syntax

<pre>
Table.PrefixColumns(<b>table</b> as table, <b>prefix</b> as text) as table
</pre>
  
## About

Returns a table where all the column names from the `table` provided are prefixed with the given text, `prefix`, plus a period in the form `prefix` `.ColumnName`.

## Example 1

Prefix the columns with "MyTable" in the table.

**Usage**

```powerquery-m
Table.PrefixColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "MyTable"
)
```

**Output**

`Table.FromRecords({[MyTable.CustomerID = 1, MyTable.Name = "Bob", MyTable.Phone = "123-4567"]})`
