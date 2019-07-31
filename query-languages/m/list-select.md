---
title: "List.Select | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Select

## Syntax

<pre>
List.Select(<b>list</b> as list, <b>selection</b> as function) as list
</pre>
  
## About  
Returns a list of values from the list `list`, that match the selection condition `selection`.

## Example 1
Find the values in the list {1, -3, 4, 9, -2} that are greater than 0.

```powerquery-m
List.Select({1, -3, 4, 9, -2}, each _ > 0)
```

<table> <tr><td>1</td></tr> <tr><td>4</td></tr> <tr><td>9</td></tr> </table>
