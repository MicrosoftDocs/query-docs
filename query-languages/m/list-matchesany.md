---
description: "Learn more about: List.MatchesAny"
title: "List.MatchesAny"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
List.MatchesAny({9, 10, 11}, each _  > 10)
```

**Output**

`true`

## Example 2

Find if any of the values in the list {1, 2, 3} are greater than 10.

**Usage**

```powerquery-m
List.MatchesAny({1, 2, 3}, each _  > 10)
```

**Output**

`false`
