---
title: "List.RemoveLastN | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveLastN

## Syntax

<pre>
List.RemoveLastN(<b>list</b> as list, optional <b>countOrCondition</b> as any) as list
</pre>
  
## About  
Returns a list that removes the last `countOrCondition` elements from the end of list `list`. If `list` has less than `countOrCondition` elements, an empty list is returned. <ul> <li>If a number is specified, up to that many items are removed. </li> <li>If a condition is specified, the returned list ends with the first element from the bottom in <code>list</code> that meets the criteria. Once an item fails the condition, no further items are considered. </li> <li>If this parameter is null, only one item is removed. </li> </ul>

## Example 1
Create a list from {1, 2, 3, 4, 5} without the last 3 numbers.

```powerquery-m
List.RemoveLastN({1, 2, 3, 4, 5}, 3)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>

## Example 2
Create a list from {5, 4, 2, 6, 4} that ends with a number less than 3.

```powerquery-m
List.RemoveLastN({5, 4, 2, 6, 4}, each _ > 3)
```

<table> <tr><td>5</td></tr> <tr><td>4</td></tr> <tr><td>2</td></tr> </table>
