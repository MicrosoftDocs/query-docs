---
description: "Learn more about: Table.ReplaceMatchingRows"
title: "Table.ReplaceMatchingRows | Microsoft Docs"
ms.date: 5/13/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.ReplaceMatchingRows

## Syntax

<pre>
Table.ReplaceMatchingRows(<b>table</b> as table, <b>replacements</b> as list, optional <b>equationCriteria</b> as any) as table 
</pre>
  
## About  
Replaces all the specified rows in the `table` with the provided ones. The rows to replace and the replacements are specified in `replacements`, using {old, new} formatting. An optional `equationCriteria` parameter may be specified to control comparison between the rows of the table.

## Example 1
Replace the rows [a = 1, b = 2] and [a = 2, b = 3] with [a = -1, b = -2],[a = -2, b = -3] in the table.

```powerquery-m
Table.ReplaceMatchingRows(
    Table.FromRecords({
        [a = 1, b = 2],
        [a = 2, b = 3],
        [a = 3, b = 4],
        [a = 1, b = 2]
    }),
    {
        {[a = 1, b = 2], [a = -1, b = -2]},
        {[a = 2, b = 3], [a = -2, b = -3]}
    }
)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>-1</td> <td>-2</td> </tr> <tr> <td>-2</td> <td>-3</td> </tr> <tr> <td>3</td> <td>4</td> </tr> <tr> <td>-1</td> <td>-2</td> </tr> </table>
