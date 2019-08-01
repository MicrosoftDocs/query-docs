---
title: "Table.TransformColumnTypes | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.TransformColumnTypes

## Syntax

<pre>
Table.TransformColumnTypes(<b>table</b> as table, <b>typeTransformations</b> as list, optional <b>culture</b> as nullable text) as table
</pre> 
  
## About  
Returns a table from the input `table` by applying the transform operation to the columns specified in the parameter `typeTransformations` (where format is { column name, type name}), using the specified culture in the parameter `culture`. If the column doesn't exist, an exception is thrown.

## Example 1
Transform the number values in column [a] to text values from the table `({[a = 1, b = 2], [a = 3, b = 4]})`.

```powerquery-m
Table.TransformColumnTypes(Table.FromRecords({[a = 1, b = 2], [a = 3, b = 4]}), {"a", type text}, "en-US")
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>1</td> <td>2</td> </tr> <tr> <td>3</td> <td>4</td> </tr> </table>
