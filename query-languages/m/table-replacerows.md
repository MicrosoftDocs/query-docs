---
title: "Table.ReplaceRows | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReplaceRows

## Syntax

<pre>
Table.ReplaceRows(<b>table</b> as table, <b>offset</b> as number, <b>count</b> as number, <b>rows</b> as list) as table 
</pre>
  
## About  
Replaces a specified number of rows, `count`, in the input `table` with the specified `rows`, beginning after the `offset`. The `rows` parameter is a list of records. <ul> <li><code>table</code>: The table where the replacement is performed.</li> <li><code>offset</code>: The number of rows to skip before making the replacement.</li> <li><code>count</code>: The number of rows to replace.</li> <li><code>rows</code>: The list of row records to insert into the <code>table</code> at the location specified by the <code>offset</code>.</li> </ul> 

## Example 1
Starting at position 1, replace 3 rows.

```powerquery-m
Table.ReplaceRows(Table.FromRecords({[Column1=1], [Column1=2], [Column1=3], [Column1=4], [Column1=5]}), 1, 3, {[Column1=6], [Column1=7]})
```

<table> <tr> <th>Column1</th> </tr> <tr> <td>1</td> </tr> <tr> <td>6</td> </tr> <tr> <td>7</td> </tr> <tr> <td>5</td> </tr> </table>
