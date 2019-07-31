---
title: "List.Distinct | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Distinct

## Syntax

<pre>
List.Distinct(<b>list</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About  
Returns a list that contains all the values in list `list` with duplicates removed. If the list is empty, the result is an empty list.

## Example 1
Remove the duplicates from the list {1, 1, 2, 3, 3, 3}.

```powerquery-m
List.Distinct({1, 1, 2, 3, 3, 3})
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> </table>
