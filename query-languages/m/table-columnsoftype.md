---
description: "Learn more about: Table.ColumnsOfType"
title: "Table.ColumnsOfType"
ms.subservice: m-source
---
# Table.ColumnsOfType

## Syntax

<pre>
Table.ColumnsOfType(<b>table</b> as table, <b>listOfTypes</b> as list) as list
</pre>
  
## About

Returns a list with the names of the columns from table `table` that match the types specified in `listOfTypes`.

## Example 1

Return the names of columns of type Number.Type from the table.

**Usage**

```powerquery-m
Table.ColumnsOfType(
    Table.FromRecords(
        {[a = 1, b = "hello"]},
        type table[a = Number.Type, b = Text.Type]
    ),
    {type number}
)
```

**Output**

`{"a"}`
