---
title: "Table.RemoveRowsWithErrors | Microsoft Docs"
ms.date: 4/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.RemoveRowsWithErrors

## Syntax

<pre>
Table.RemoveRowsWithErrors(<b>table</b> as table, optional <b>columns</b> as nullable list) as table
</pre>
  
## About  
Returns a table with the rows removed from the input table that contain an error in at least one of the cells. If a columns list is specified, then only the cells in the specified columns are inspected for errors.

## Example 1
Remove error value from first row.

```powerquery-m
Table.RemoveRowsWithErrors(
    Table.FromRecords({
        [Column1 = ...],
        [Column1 = 2],
        [Column1 = 3]
    })
)
```

<table> <tr> <th>Column1</th> </tr> <tr> <td>2</td> </tr> <tr> <td>3</td> </tr> </table>
