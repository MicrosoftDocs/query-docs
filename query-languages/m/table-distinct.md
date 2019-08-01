---
title: "Table.Distinct | Microsoft Docs"
ms.date: 8/1/201
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.Distinct

## Syntax

<pre>
Table.Distinct(<b>table</b> as table, optional <b>equationCriteria</b> as any) as table
</pre>
  
## About  
Removes duplicate rows from the table `table`. An optional parameter, `equationCriteria`, specifies which columns of the table are tested for duplication. If `equationCriteria` is not specified, all columns are tested.

## Example 1
Remove the duplicate rows from the table.

```powerquery-m
Table.Distinct(Table.FromRecords({[a = "A", b = "a"], [a = "B", b = "b"], [a = "A", b = "a"]}))
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>A</td> <td>a</td> </tr> <tr> <td>B</td> <td>b</td> </tr> </table>

## Example 2
Remove the duplicate rows from column [b] in the table `({[a = "A", b = "a"], [a = "B", b = "a"], [a = "A", b = "b"]})`.

```powerquery-m
Table.Distinct(Table.FromRecords({[a = "A", b = "a"], [a = "B", b = "a"], [a = "A", b = "b"]}), "b")
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>A</td> <td>a</td> </tr> <tr> <td>A</td> <td>b</td> </tr> </table>
