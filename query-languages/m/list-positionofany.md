---
description: "Learn more about: List.PositionOfAny"
title: "List.PositionOfAny | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.PositionOfAny

## Syntax

<pre>
List.PositionOfAny(<b>list</b> as list, <b>values</b> as list, optional <b>occurrence</b> as nullable number, optional <b>equationCriteria</b> as any) as any
</pre>
  
## About  
Returns the offset in list `list` of the first occurrence of a value in a list `values`. Returns -1 if no occurrence is found. An optional occurrence parameter `occurrence` can be specified. <ul> <li><code>occurrence</code>: The maximum number of occurrences that can be returned.</li> </ul>

## Example 1
Find the first position in the list {1, 2, 3} at which the value 2 or 3 appears.

```powerquery-m
List.PositionOfAny({1, 2, 3}, {2, 3})
```

`1`
