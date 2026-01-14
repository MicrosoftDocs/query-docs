---
description: "Learn more about: Table.ReorderColumns"
title: "Table.ReorderColumns"
ms.subservice: m-source
ms.topic: reference
---
# Table.ReorderColumns

## Syntax

<pre>
Table.ReorderColumns(
    <b>table</b> as table,
    <b>columnOrder</b> as list,
    optional <b>missingField</b> as nullable number
) as table
</pre>
  
## About

Returns a table from the input `table`, with the columns in the order specified by `columnOrder`. Columns that are not specified in the list will not be reordered. If the column doesn't exist, an exception is thrown unless the optional parameter `missingField` specifies an alternative (eg. [MissingField.UseNull](missingfield-type.md) or [MissingField.Ignore](missingfield-type.md)).

## Example 1

Switch the order of the columns [Phone] and [Name] in the table.

**Usage**

```powerquery-m
Table.ReorderColumns(
    Table.FromRecords({[CustomerID = 1, Phone = "123-4567", Name = "Bob"]}),
    {"Name", "Phone"}
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`

## Example 2

Switch the order of the columns [Phone] and [Address] or use "MissingField.Ignore" in the table. It doesn't change the table because column [Address] doesn't exist.

**Usage**

```powerquery-m
Table.ReorderColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    {"Phone", "Address"},
    MissingField.Ignore
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`
