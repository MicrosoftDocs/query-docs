---
title: "Table.PositionOfAny | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.PositionOfAny

## Syntax

<pre> 
Table.PositionOfAny(<b>table</b> as table, <b>rows</b> as list, optional <b>occurrence</b> as nullable number, optional <b>equationCriteria</b> as any) as any
</pre>
  
## About  
Returns the row(s) position(s) from the `table` of the first occurrence of the list of `rows`. Returns -1 if no occurrence is found. <ul> <li><code>table</code>: The input table.</li> <li><code>rows</code>: The list of rows in the table to find the positions of.</li> <li><code>occurrence</code>: <i>[Optional]</i> Specifies which occurrences of the row to return.</li> <li><code>equationCriteria</code>: <i>[Optional]</i> Controls the comparison between the table rows.</li> </ul> 

## Example 1
Find the position of the first occurrence of [a = 2, b = 4] or [a = 6, b = 8] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

```powerquery-m
Table.PositionOfAny(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 1, b = 4],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    {
        [a = 2, b = 4],
        [a = 6, b = 8]
    }
)
```

`0`

## Example 2
Find the position of all the occurrences of [a = 2, b = 4] or [a = 6, b = 8] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]}`.

```powerquery-m
Table.PositionOfAny(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 6, b = 8],
        [a = 2, b = 4],
        [a = 1, b = 4]
    }),
    {
        [a = 2, b = 4],
        [a = 6, b = 8]
    },
    Occurrence.All
)
```

<table> <tr><td>0</td></tr> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>
