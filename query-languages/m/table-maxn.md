---
title: "Table.MaxN | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.MaxN

## Syntax

<pre>
Table.MaxN(<b>table</b> as table, <b>comparisonCriteria</b> as any, <b>countOrCondition</b> as any) as table
</pre>
  
## About  
Returns the largest row(s) in the `table`, given the `comparisonCriteria`. After the rows are sorted, the `countOrCondition` parameter must be specified to further filter the result. Note the sorting algorithm cannot guarantee a fixed sorted result. The `countOrCondition` parameter can take multiple forms: <ul> <li> If a number is specified, a list of up to <code>countOrCondition</code> items in ascending order is returned. </li> <li> If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered. </li> </ul>

## Example 1
Find the row with the largest value in column [a] with the condition [a] > 0, in the table. The rows are sorted before the filter is applied.

```powerquery-m
Table.MaxN(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 0, b = 0],
        [a = 6, b = 2]
    }),
    "a",
    each [a] > 0
)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>6</td> <td>2</td> </tr> <tr> <td>2</td> <td>4</td> </tr> </table>

## Example 2
Find the row with the largest value in column [a] with the condition [b] > 0, in the table. The rows are sorted before the filter is applied.

```powerquery-m
Table.MaxN(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 8, b = 0],
        [a = 6, b = 2]
    }),
    "a",
    each [b] > 0
)
```

<table> <tr> </tr> </table>
