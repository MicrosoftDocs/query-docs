---
description: "Learn more about: Table.PrefixColumns"
title: "Table.PrefixColumns | Microsoft Docs"
ms.date: 4/24/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

```powerquery-m
Table.PrefixColumns(
    Table.FromRecords({[CustomerID = 1, Name = "Bob", Phone = "123-4567"]}),
    "MyTable"
)
```

<table> <tr> <th>MyTable.CustomerID</th> <th>MyTable.Name</th> <th>MyTable.Phone</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>123-4567</td> </tr> </table>
