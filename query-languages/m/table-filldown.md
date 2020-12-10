---
title: "Table.FillDown | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FillDown

## Syntax

<pre>
Table.FillDown(<b>table</b> as table, <b>columns</b> as list) as table
</pre>

## About
Returns a table from the `table` specified where the value of a previous cell is propagated to the null-valued cells below in the `columns` specified.

## Example 1
Return a table with the null values in column [Place] filled with the value above them from the table.

```powerquery-m
Table.FillDown(
    Table.FromRecords({
        [Place = 1, Name = "Bob"],
        [Place = null, Name = "John"],
        [Place = 2, Name = "Brad"],
        [Place = 3, Name = "Mark"],
        [Place = null, Name = "Tom"],
        [Place = null, Name = "Adam"]
    }),
    {"Place"}
)
```

<table> <tr> <th>Place</th> <th>Name</th> </tr> <tr> <td>1</td> <td>Bob</td> </tr> <tr> <td>1</td> <td>John</td> </tr> <tr> <td>2</td> <td>Brad</td> </tr> <tr> <td>3</td> <td>Mark</td> </tr> <tr> <td>3</td> <td>Tom</td> </tr> <tr> <td>3</td> <td>Adam</td> </tr> </table>

  
