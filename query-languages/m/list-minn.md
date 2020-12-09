---
title: "List.MinN | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.MinN

## Syntax

<pre>
List.MinN(<b>list</b> as list, <b>countOrCondition</b> as any, optional <b>comparisonCriteria</b> as any, optional <b>includeNulls</b> as nullable logical) as list
</pre>
  
## About  
Returns the minimum value(s) in the list, `list`. The parameter, `countOrCondition`, specifies the number of values to return or a filtering condition. The optional parameter, `comparisonCriteria`, specifies how to compare values in the list. <ul> <li> <code>list</code>: The list of values.</li> <li> <code>countOrCondition</code>: If a number is specified, a list of up to <code>countOrCondition</code> items in ascending order is returned. If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered. If this parameter is null the single smallest value in the list is returned.</li> <li><code>comparisonCriteria</code>: <i>[Opional]</i> An optional <code>comparisonCriteria</code> value, may be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used. </ul>

## Example 1
Find the 5 smallest values in the list `{3, 4, 5, -1, 7, 8, 2}`.

```powerquery-m
List.MinN({3, 4, 5, -1, 7, 8, 2}, 5)
```

<table> <tr><td>-1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>
