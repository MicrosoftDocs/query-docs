---
description: "Learn more about: Table.ExpandListColumn"
title: "Table.ExpandListColumn | Microsoft Docs"
ms.date: 5/13/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ExpandListColumn

## Syntax

<pre>
Table.ExpandListColumn(<b>table</b> as table, <b>column</b> as text) as table
</pre>
  
## About  
Given a `table`, where a `column` is a list of values, splits the list into a row for each value. Values in the other columns are duplicated in each new row created.

## Example 1
Split the list column [Name] in the table.

```powerquery-m
Table.ExpandListColumn(
    Table.FromRecords({[Name = {"Bob", "Jim", "Paul"}, Discount = .15]}),
    "Name"
)
```

<table> <tr> <th>Name</th> <th>Discount</th> </tr> <tr> <td>Bob</td> <td>0.15</td> </tr> <tr> <td>Jim</td> <td>0.15</td> </tr> <tr> <td>Paul</td> <td>0.15</td> </tr> </table>
