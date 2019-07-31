---
title: "List.ContainsAny | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.ContainsAny

## Syntax

<pre>
List.ContainsAny(<b>list</b> as list, <b>values</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>
  
## About  
Indicates whether the list `list` includes any of the values in another list, `values`. Returns true if value is found in the list, false otherwise. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing. 

## Example 1
Find out if the list {1, 2, 3, 4, 5} contains 3 or 9.

```powerquery-m
List.ContainsAny({1, 2, 3, 4, 5}, {3, 9})
```

`true`

## Example 2
Find out if the list {1, 2, 3, 4, 5} contains 6 or 7.

```powerquery-m
List.ContainsAny({1, 2, 3, 4, 5}, {6, 7})
```

`false`
