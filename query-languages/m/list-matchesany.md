---
description: "Learn more about: List.MatchesAny"
title: "List.MatchesAny | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.MatchesAny

## Syntax

<pre>
List.MatchesAny(<b>list</b> as list, <b>condition</b> as function) as logical
</pre>
  
## About  
Returns `true` if the condition function, `condition`, is satisfied by any of values in the list `list`, otherwise returns `false`.

## Example 1
Find if any of the values in the list {9, 10, 11} are greater than 10.

```powerquery-m
List.MatchesAny({9, 10, 11}, each _  > 10)
```

`true`

## Example 2
Find if any of the values in the list {1, 2, 3} are greater than 10.

```powerquery-m
List.MatchesAny({1, 2, 3}, each _  > 10)
```

`false`
