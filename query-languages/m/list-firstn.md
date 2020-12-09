---
title: "List.FirstN | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.FirstN

## Syntax

<pre>
List.FirstN(<b>list</b> as list, <b>countOrCondition</b> as any) as any
</pre>
  
## About  
 <ul> <li>If a number is specified, up to that many items are returned. </li> <li>If a condition is specified, all items are returned that initially meet the condition. Once an item fails the condition, no further items are considered. </li> </ul>

## Example 1
Find the intial values in the list {3, 4, 5, -1, 7, 8, 2} that are greater than 0.

```powerquery-m
List.FirstN({3, 4, 5, -1, 7, 8, 2}, each _ > 0)
```

<table> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>
