---
title: "List.AllTrue | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.AllTrue

## Syntax

<pre>
List.AllTrue(<b>list</b> as list) as logical
</pre>
  
## About  
Returns true if all expressions in the list `list` are true.

## Example 1
Determine if all the expressions in the list {true, true, 2 > 0} are true.

```powerquery-m
List.AllTrue({true, true, 2 > 0})
```

`true`

## Example 2
Determine if all the expressions in the list {true, true, 2 < 0} are true.

```powerquery-m
List.AllTrue({true, false, 2 < 0})
```

`false`
