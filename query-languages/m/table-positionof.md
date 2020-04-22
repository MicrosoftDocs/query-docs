---
title: "Table.PositionOf | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.PositionOf

## Syntax

<pre>
Table.PositionOf(<b>table</b> as table, <b>row</b> as record, optional <b>occurrence</b> as any, optional <b>equationCriteria</b> as any) as any
</pre>
  
## About  
Returns the row position of the first occurrence of the `row` in the `table` specified. Returns -1 if no occurrence is found. <ul> <li><code>table</code>: The input table.</li> <li><code>row</code>: The row in the table to find the position of.</li> <li><code>occurrence</code>: <i>[Optional]</i> Specifies which occurrences of the row to return.</li> <li><code>equationCriteria</code>: <i>[Optional]</i> Controls the comparison between the table rows.</li> </ul> 

## Example 1
Find the position of the first occurrence of [a = 2, b = 4] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

```powerquery-m
Table.PositionOf(
    Table.FromRecords({
        [a = 2, b = 4], 
        [a = 1, b = 4], 
        [a = 2, b = 4], 
        [a = 1, b = 4]
    }), 
    [a = 2, b = 4]
)
```

`0`

## Example 2
Find the position of the second occurrence of [a = 2, b = 4] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

```powerquery-m
Table.PositionOf(
    Table.FromRecords({
        [a = 2, b = 4], 
        [a = 1, b = 4], 
        [a = 2, b = 4], 
        [a = 1, b = 4]
    }), 
    [a = 2, b = 4], 
    1
)
```

`2`

## Example 3
Find the position of all the occurrences of [a = 2, b = 4] in the table `({[a = 2, b = 4], [a = 6, b = 8], [a = 2, b = 4], [a = 1, b = 4]})`.

```powerquery-m
Table.PositionOf(
    Table.FromRecords({
        [a = 2, b = 4], 
        [a = 1, b = 4], 
        [a = 2, b = 4], 
        [a = 1, b = 4]
    }), 
    [a = 2, b = 4], 
    Occurrence.All
)
```

<table> <tr><td>0</td></tr> <tr><td>2</td></tr> </table>
