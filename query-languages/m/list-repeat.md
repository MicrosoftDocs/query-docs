---
title: "List.Repeat | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Repeat

## Syntax

<pre>
List.Repeat(<b>list</b> as list, <b>count</b> as number) as list
</pre>
  
## About  
Returns a list that is `count` repetitions of the original list, `list`.

## Example 1
Create a list that has {1, 2} repeated 3 times.

```powerquery-m
List.Repeat({1, 2}, 3)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>
