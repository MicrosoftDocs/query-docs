---
description: "Learn more about: Table.RemoveColumns"
title: "Table.RemoveColumns"
---
# Table.RemoveColumns

## Syntax

<pre>
Table.RemoveColumns(<b>table</b> as table, <b>columns</b> as any, optional <b>missingField</b> as nullable number) as table
</pre>
  
## About

Removes the specified `columns` from the `table` provided. If the specified column doesn't exist, an error is raised unless the optional parameter `missingField` specifies an alternative behavior (for example, [MissingField.UseNull](missingfield-type.md) or [MissingField.Ignore](missingfield-type.md)).

## Example 1

Remove column [Phone] from the table.

**Usage**

```powerquery-m
Table.RemoveColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "Phone"
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob"]})`

### Example 2

Try to remove a non-existent column from the table.

**Usage**

```powerquery-m
Table.RemoveColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "Address"
)
```

**Output**

`[Expression.Error] The column 'Address' of the table wasn't found.`
