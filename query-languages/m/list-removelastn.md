---
description: "Learn more about: List.RemoveLastN"
title: "List.RemoveLastN"
ms.date: 3/9/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.RemoveLastN

## Syntax

<pre>
List.RemoveLastN(<b>list</b> as list, optional <b>countOrCondition</b> as any) as list
</pre>
  
## About

Returns a list that removes the last `countOrCondition` elements from the end of list `list`. If `list` has less than `countOrCondition` elements, an empty list is returned.

* If a number is specified, up to that many items are removed.
* If a condition is specified, the returned list ends with the first element from the bottom in `list` that meets the criteria. Once an item fails the condition, no further items are considered.
* If this parameter is null, only one item is removed.

## Example 1

Create a list from {1, 2, 3, 4, 5} without the last 3 numbers.

**Usage**

```powerquery-m
List.RemoveLastN({1, 2, 3, 4, 5}, 3)
```

**Output**

`{1, 2}`

## Example 2

Create a list from {5, 4, 2, 6, 4} that ends with a number less than 3.

**Usage**

```powerquery-m
List.RemoveLastN({5, 4, 2, 6, 4}, each _ > 3)
```

**Output**

`{5, 4, 2}`
