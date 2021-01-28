---
description: "Learn more about: List.RemoveRange"
title: "List.RemoveRange | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.RemoveRange

## Syntax

<pre>
List.RemoveRange(<b>list</b> as list, <b>index</b> as number, optional <b>count</b> as nullable number) as list
</pre>
  
## About  
Removes `count` values in the `list` starting at the specified position, `index`.

## Example 1
Remove 3 values in the list {1, 2, 3, 4, -6, -2, -1, 5} starting at index 4.

```powerquery-m
List.RemoveRange({1, 2, 3, 4, -6, -2, -1, 5}, 4, 3)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>
