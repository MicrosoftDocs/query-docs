---
description: "Learn more about: Table.RemoveColumns"
title: "Table.RemoveColumns | Microsoft Docs"
ms.date: 3/10/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.RemoveColumns

## Syntax

<pre>
Table.RemoveColumns(<b>table</b> as table, <b>columns</b> as any, optional <b>missingField</b> as nullable number) as table
</pre>
  
## About

Removes the specified `columns` from the `table` provided. If the column doesn't exist, an exception is thrown unless the optional parameter `missingField` specifies an alternative (eg. `MissingField.UseNull` or `MissingField.Ignore`).

## Example 1

Remove column [Phone] from the table.

**Usage**

```powerquery-m
Table.RemoveColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "Phone"

```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob"]})`

### Example 2

Remove column [Address] from the table. Throws an error if it doesn't exist.

**Usage**

```powerquery-m
Table.RemoveColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "Address"
)
```

**Output**

`[Expression.Error] The field 'Address' of the record was not found.`
