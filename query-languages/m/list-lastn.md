---
description: "Learn more about: List.LastN"
title: "List.LastN | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.LastN

## Syntax

<pre>
List.LastN(<b>list</b> as list, optional <b>countOrCondition</b> as any) as any
</pre>
  
## About

Returns the last item of the list `list`. If the list is empty, an exception is thrown. This function takes an optional parameter, `countOrCondition`, to support gathering multiple items or filtering items. `countOrCondition` can be specified in three ways:

* If a number is specified, up to that many items are returned.
* If a condition is specified, all items are returned that initially meet the condition, starting at the end of the list. Once an item fails the condition, no further items are considered.
* If this parameter is null the last item in the list is returned.

## Example 1

Find the last value in the list {3, 4, 5, -1, 7, 8, 2}.

**Usage**

```powerquery-m
List.LastN({3, 4, 5, -1, 7, 8, 2}, 1)
```

**Output**

`{2}`

## Example 2

Find the last values in the list {3, 4, 5, -1, 7, 8, 2} that are greater than 0.

**Usage**

```powerquery-m
List.LastN({3, 4, 5, -1, 7, 8, 2}, each _ > 0)
```

**Output**

`{7, 8, 2}`
