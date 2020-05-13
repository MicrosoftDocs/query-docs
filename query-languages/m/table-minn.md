---
title: "Table.MinN | Microsoft Docs"
ms.date: 5/13/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.MinN

## Syntax

<pre>
Table.MinN(<b>table</b> as table, <b>comparisonCriteria</b> as any, <b>countOrCondition</b> as any) as table
</pre>
  
## About  
Returns the smallest row(s) in the `table`, given the `comparisonCriteria`. After the rows are sorted, the `countOrCondition` parameter must be specified to further filter the result. Note the sorting algorithm cannot guarantee a fixed sorted result. The `countOrCondition` parameter can take multiple forms: <ul> <li> If a number is specified, a list of up to <code>countOrCondition</code> items in ascending order is returned. </li> <li> If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered. </li> </ul>

## Example 1
Find the row with the smallest value in column [a] with the condition [a] < 3, in the table. The rows are sorted before the filter is applied.

```powerquery-m
Table.MinN( 
    Table.FromRecords({ 
        [a = 2, b = 4],
        [a = 0, b = 0],
        [a = 6, b = 4]
    }), 
    "a", 
    each [a] < 3 
)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>0</td> <td>0</td> </tr> <tr> <td>2</td> <td>4</td> </tr> </table>

## Example 2
Find the row with the smallest value in column [a] with the condition [b] < 0, in the table. The rows are sorted before the filter is applied.

```powerquery-m
Table.MinN(
    Table.FromRecords({
        [a = 2, b = 4],
        [a = 8, b = 0],
        [a = 6, b = 2]
    }),
    "a",
    each [b] < 0
)
```

<table> <tr> </tr> </table>
