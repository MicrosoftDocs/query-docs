---
title: "Table.FillUp | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.FillUp

## Syntax

<pre>
Table.FillUp(<b>table</b> as table, <b>columns</b> as list) as table
</pre>

## About
Returns a table from the `table` specified where the value of the next cell is propagated to the null-valued cells above in the `columns` specified.

## Example 1
Return a table with the null values in column [Column2] filled with the value below them from the table.

```powerquery-m
Table.FillUp(Table.FromRecords({[Column1 = 1, Column2 = 2], [Column1 = 3, Column2 = null], [Column1 = 5, Column2 = 3]}), {"Column2"})
```

<table> <tr> <th>Column1</th> <th>Column2</th> </tr> <tr> <td>1</td> <td>2</td> </tr> <tr> <td>3</td> <td>3</td> </tr> <tr> <td>5</td> <td>3</td> </tr> </table>
