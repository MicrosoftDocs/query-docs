---
title: "List.ReplaceMatchingItems | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.ReplaceMatchingItems

## Syntax

<pre>
List.ReplaceMatchingItems(<b>list</b> as list, <b>replacements</b> as list, optional <b>equationCriteria</b> as any) as list 
</pre>
  
## About  
Performs the given replacements to the list `list`. A replacement operation `replacements` consists of a list of two values, the old value and new value, provided in a list. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1
Create a list from {1, 2, 3, 4, 5} replacing the value 5 with -5, and the value 1 with -1.

```powerquery-m
List.ReplaceMatchingItems({1, 2, 3, 4, 5}, {{5, -5}, {1, -1}})
```

<table> <tr><td>-1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>-5</td></tr> </table>
