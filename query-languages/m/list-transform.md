---
title: "List.Transform | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Transform

## Syntax

<pre>
List.Transform(<b>list</b> as list, <b>transform</b> as function) as list
</pre>
  
## About  
Returns a new list of values by applying the transform function `transform` to the list, `list`.

## Example 1
Add 1 to each value in the list {1, 2}.

```powerquery-m
List.Transform({1, 2}, each _ + 1)
```

<table> <tr><td>2</td></tr> <tr><td>3</td></tr> </table>
