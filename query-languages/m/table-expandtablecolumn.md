---
title: "Table.ExpandTableColumn | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ExpandTableColumn

## Syntax

<pre>
Table.ExpandTableColumn(<b>table</b> as table, <b>column</b> as text, <b>columnNames</b> as list, optional <b>newColumnNames</b> as nullable list) as table
</pre>
  
## About  
Expands tables in `table`[`column`] into multiple rows and columns. `columnNames` is used to select the columns to expand from the inner table. Specify `newColumnNames` to avoid conflicts between existing columns and new columns.

## Example 1
Expand table columns in `[a]` in the table `({[t = {[a=1, b=2, c=3], [a=2,b=4,c=6]}, b = 2]})` into 3 columns `[t.a]`, `[t.b]` and `[t.c]`.

```powerquery-m
Table.ExpandTableColumn(Table.FromRecords({[t = Table.FromRecords({[a=1, b=2, c= 3],[a=2,b=4,c=6]}), b = 2]}), "t", {"a","b","c"}, {"t.a","t.b","t.c"})
```

<table> <tr> <th>t.a</th> <th>t.b</th> <th>t.c</th> <th>b</th> </tr> <tr> <td>1</td> <td>2</td> <td>3</td> <td>2</td> </tr> <tr> <td>2</td> <td>4</td> <td>6</td> <td>2</td> </tr> </table>
