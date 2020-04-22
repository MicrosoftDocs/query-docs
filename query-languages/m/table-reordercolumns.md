---
title: "Table.ReorderColumns | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.ReorderColumns

## Syntax

<pre>
Table.ReorderColumns(<b>table</b> as table, <b>columnOrder</b> as list, optional <b>missingField</b> as nullable number) as table
</pre> 
  
## About  
Returns a table from the input `table`, with the columns in the order specified by `columnOrder`. Columns that are not specified in the list will not be reordered. If the column doesn't exist, an exception is thrown unless the optional parameter `missingField` specifies an alternative (eg. `MissingField.UseNull` or `MissingField.Ignore`).

## Example 1
Switch the order of the columns [Phone] and [Name] in the table.

```powerquery-m
Table.ReorderColumns(
    Table.FromRecords({[CustomerID=1, Phone = "123-4567", Name ="Bob"]}),
    {"Name","Phone"}
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> </table>

## Example 2
Switch the order of the columns [Phone] and [Address] or use "MissingField.Ignore" in the table. It doesn't change the table because column [Address] doesn't exist.

```powerquery-m
Table.ReorderColumns(
    Table.FromRecords({[CustomerID=1, Name = "Bob", Phone = "123-4567"]}), 
    {"Phone", "Address"}, 
    MissingField.Ignore
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> <th>Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> </table>
