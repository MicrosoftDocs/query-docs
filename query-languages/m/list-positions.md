---
description: "Learn more about: List.Positions"
title: "List.Positions | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Positions

## Syntax

<pre>
List.Positions(<b>list</b> as list) as list
</pre>
  
## About  
Returns a list of offsets for the input list `list`. When using List.Transform to change a list, the list of positions can be used to give the transform access to the position.

## Example 1
Find the offsets of values in the list {1, 2, 3, 4, null, 5}.

```powerquery-m
List.Positions({1, 2, 3, 4, null, 5})
```

<table> <tr><td>0</td></tr> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>
