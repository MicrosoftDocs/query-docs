---
description: "Learn more about: Table.HasColumns"
title: "Table.HasColumns"
ms.date: 3/14/2022
---
# Table.HasColumns

## Syntax

<pre>
Table.HasColumns(<b>table</b> as table, <b>columns</b> as any) as logical 
</pre>
  
## About

indicates whether the `table` contains the specified column(s), `columns`. Returns `true` if the table contains the column(s), `false` otherwise.

## Example 1

Determine if the table has the column [Name].

**Usage**

```powerquery-m
TTable.HasColumns(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Name"
)
```

**Output**

`true`

## Example 2

Find if the table has the column [Name] and [PhoneNumber].

**Usage**

```powerquery-m
Table.HasColumns(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    {"Name", "PhoneNumber"}
)
```

**Output**

`false`
