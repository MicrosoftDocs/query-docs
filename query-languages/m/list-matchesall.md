---
description: "Learn more about: List.MatchesAll"
title: "List.MatchesAll"
ms.date: 3/11/2022
---
# List.MatchesAll

## Syntax

<pre>
List.MatchesAll(<b>list</b> as list, <b>condition</b> as function) as logical
</pre>
  
## About

Returns `true` if the condition function, `condition`, is satisfied by all values in the list `list`, otherwise returns `false`.

## Example 1

Determine if all the values in the list {11, 12, 13} are greater than 10.

**Usage**

```powerquery-m
List.MatchesAll({11, 12, 13}, each _  > 10)
```

**Output**

`true`

## Example 2

Determine if all the values in the list {1, 2, 3} are greater than 10.

**Usage**

```powerquery-m
List.MatchesAll({1, 2, 3}, each _  > 10)
```

**Output**

`false`
