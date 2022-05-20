---
description: "Learn more about: List.Difference"
title: "List.Difference | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Difference

<pre>
List.Difference(<b>list1</b> as list, <b>list2</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About

Returns the items in list `list1` that do not appear in list `list2`. Duplicate values are supported. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Find the items in list {1, 2, 3, 4, 5} that do not appear in {4, 5, 3}.

**Usage**

```powerquery-m
List.Difference({1, 2, 3, 4, 5}, {4, 5, 3})
```

**Output**

`{1, 2}`

## Example 2

Find the items in the list {1, 2} that do not appear in {1, 2, 3}.

**Usage**

```powerquery-m
List.Difference({1, 2}, {1, 2, 3})
```

**Output**

`{}`
