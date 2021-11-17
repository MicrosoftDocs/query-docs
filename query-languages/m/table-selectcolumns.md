---
description: "Learn more about: Table.SelectColumns"
title: "Table.SelectColumns | Microsoft Docs"
ms.date: 11/17/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.SelectColumns

## Syntax

<pre>
Table.SelectColumns(<b>table</b> as table, <b>columns</b> as any, optional <b>missingField</b> as nullable number) as table
</pre>
  
## About

Returns the `table` with only the specified `columns`.

* `table`: The provided table.
* `columns`: The list of columns from the table `table` to return. Columns in the returned table are in the order listed in `columns`.
* `missingField`: *(Optional)* What to do if the column does not exist. Example: `MissingField.UseNull` or `MissingField.Ignore`.

## Example 1

Only include column [Name].

```powerquery-m
Table.SelectColumns(
    Table.FromRecords({
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"],
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"],
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]
    }),
    "Name"
)
```

<table> <tr> <th>Name</th> </tr> <tr> <td>Bob</td> </tr> <tr> <td>Jim</td> </tr> <tr> <td>Paul</td> </tr> <tr> <td>Ringo</td> </tr> </table>

## Example 2

Only include columns [CustomerID] and [Name].

```powerquery-m
Table.SelectColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    {"CustomerID", "Name"}
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> </tr> <tr> <td>1</td> <td>Bob</td> </tr> </table>

## Example 3

If the included column does not exist, the default result is an error.

```powerquery-m
Table.SelectColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "NewColumn"
)
```

`[Expression.Error] The field 'NewColumn' of the record wasn't found.`

## Example 4

If the included column does not exist, option `MissingField.UseNull` creates a column of null values.

```powerquery-m
Table.SelectColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    {"CustomerID", "NewColumn"},
    MissingField.UseNull
)
```

<table> <tr> <th>CustomerID</th> <th>NewColumn</th> </tr> <tr> <td>1</td> <td></td> </tr> </table>
