---
description: "Learn more about: List.Contains"
title: "List.Contains | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Contains

## Syntax

<pre>
List.Contains(<b>list</b> as list, <b>value</b> as any, optional <b>equationCriteria</b> as any) as logical 
</pre>
  
## About  
Indicates whether the list `list` contains the value `value`. Returns true if value is found in the list, false otherwise. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing. 

## Example 1
Find if the list {1, 2, 3, 4, 5} contains 3.

```powerquery-m
List.Contains({1, 2, 3, 4, 5}, 3)
```

`true`

## Example 2
Find if the list {1, 2, 3, 4, 5} contains 6.

```powerquery-m
List.Contains({1, 2, 3, 4, 5}, 6)
```

`false`
