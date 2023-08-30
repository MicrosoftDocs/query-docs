---
description: "Learn more about: Table.RenameColumns"
title: "Table.RenameColumns"
---
# Table.RenameColumns

## Syntax

<pre>
Table.RenameColumns(<b>table</b> as table, <b>renames</b> as list, optional <b>missingField</b> as nullable number) as table
</pre>
  
## About

Performs the given renames to the columns in table `table`. A replacement operation `renames` consists of a list of two values, the old column name and new column name, provided in a list. If the column doesn't exist, an exception is thrown unless the optional parameter `missingField` specifies an alternative (eg. `MissingField.UseNull` or `MissingField.Ignore`).

## Example 1

Replace the column name "CustomerNum" with "CustomerID" in the table.

**Usage**

```powerquery-m
Table.RenameColumns(
    Table.FromRecords({[CustomerNum = 1, Name = "Bob", Phone = "123-4567"]}),
    {"CustomerNum", "CustomerID"}
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`

## Example 2

Replace the column name "CustomerNum" with "CustomerID" and "PhoneNum" with "Phone" in the table.

**Usage**

```powerquery-m
Table.RenameColumns(
    Table.FromRecords({[CustomerNum = 1, Name = "Bob", PhoneNum = "123-4567"]}),
    {
        {"CustomerNum", "CustomerID"},
        {"PhoneNum", "Phone"}
    }
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`

## Example 3

Replace the column name "NewCol" with "NewColumn" in the table, and ignore if the column doesn't exist.

**Usage**

```powerquery-m
Table.RenameColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    {"NewCol", "NewColumn"},
    MissingField.Ignore
)
```

**Output**

`Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]})`
