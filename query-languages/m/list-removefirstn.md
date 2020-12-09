---
title: "List.RemoveFirstN | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.RemoveFirstN

## Syntax

<pre>
List.RemoveFirstN(<b>list</b> as list, optional <b>countOrCondition</b> as any) as list
</pre>
  
## About  
Returns a list that removes the first element of list `list`. If `list` is an empty list an empty list is returned. This function takes an optional parameter, `countOrCondition`, to support removing multiple values as listed below. <ul> <li>If a number is specified, up to that many items are removed. </li> <li>If a condition is specified, the returned list begins with the first element in <code>list</code> that meets the criteria. Once an item fails the condition, no further items are considered. </li> <li>If this parameter is null, the default behavior is observed. </li> </ul>

## Example 1
Create a list from {1, 2, 3, 4, 5} without the first 3 numbers.

```powerquery-m
List.RemoveFirstN({1, 2, 3, 4, 5}, 3)
```

<table> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>

## Example 2
Create a list from {5, 4, 2, 6, 1} that starts with a number less than 3.

```powerquery-m
List.RemoveFirstN({5, 4, 2, 6, 1}, each _ > 3)
```

<table> <tr><td>2</td></tr> <tr><td>6</td></tr> <tr><td>1</td></tr> </table>
