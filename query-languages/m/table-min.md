---
title: "Table.Min | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Min

## Syntax

<pre>
Table.Min(<b>table</b> as table, <b>comparisonCriteria</b> as any, optional <b>default</b> as any) as any
</pre>
  
## About  
Returns the smallest row in the `table`, given the `comparisonCriteria`. If the table is empty, the optional `default` value is returned.

## Example 1
Find the row with the smallest value in column [a] in the table.

```powerquery-m
Table.Min(Table.FromRecords({[a = 2, b = 4], [a = 6, b = 8]}), "a")
```

<table> <tr> <th>a</th> <td>2</td> </tr> <tr> <th>b</th> <td>4</td> </tr> </table>

## Example 2
Find the row with the smallest value in column [a] in the table. Return -1 if empty.

```powerquery-m
Table.Min(#table({"a"},{}), "a", -1)
```

`-1`
