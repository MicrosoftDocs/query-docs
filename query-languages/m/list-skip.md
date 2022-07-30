---
description: "Learn more about: List.Skip"
title: "List.Skip"
ms.date: 3/9/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Skip

## Syntax

<pre>
List.Skip(<b>list</b> as list, optional <b>countOrCondition</b> as any) as list
</pre>
  
## About

Returns a list that skips the first element of list `list`. If `list` is an empty list an empty list is returned. This function takes an optional parameter, `countOrCondition`, to support skipping multiple values as listed below.

* If a number is specified, up to that many items are skipped.
* If a condition is specified, the returned list begins with the first element in `list` that meets the criteria. Once an item fails the condition, no further items are considered.
* If this parameter is null, the default behavior is observed.

## Example 1

Create a list from {1, 2, 3, 4, 5} without the first 3 numbers.

**Usage**

```powerquery-m
List.Skip({1, 2, 3, 4, 5}, 3)
```

**Output**

`{4, 5}`

## Example 2

Create a list from {5, 4, 2, 6, 1} that starts with a number less than 3.

**Usage**

```powerquery-m
List.Skip({5, 4, 2, 6, 1}, each _ > 3)
```

**Output**

`{2, 6, 1}`
