---
description: "Learn more about: List.Intersect"
title: "List.Intersect | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Intersect

## Syntax

<pre>
List.Intersect(<b>lists</b> as list, optional <b>equationCriteria</b> as any) as list 
</pre>
  
## About  
Returns the intersection of the list values found in the input list `lists`. An optional parameter, `equationCriteria`, can be specifed.

## Example 1
Find the intersection of the lists {1..5}, {2..6}, {3..7}.

```powerquery-m
List.Intersect({{1..5}, {2..6}, {3..7}})
```

<table> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>
