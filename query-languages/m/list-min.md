---
description: "Learn more about: List.Min"
title: "List.Min | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Min

## Syntax

<pre>
List.Min(<b>list</b> as list, optional <b>default</b> as any, optional <b>comparisonCriteria</b> as any, optional <b>includeNulls</b> as nullable logical) as any
</pre>
  
## About

Returns the minimum item in the list `list`, or the optional default value `default` if the list is empty. An optional comparisonCriteria value, `comparisonCriteria`, may be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used.

## Example 1

Find the min in the list {1, 4, 7, 3, -2, 5}.

**Usage**

```powerquery-m
List.Min({1, 4, 7, 3, -2, 5})
```

**Output**

`-2`

## Example 2

Find the min in the list {} or return -1 if it is empty.

**Usage**

```powerquery-m
List.Min({}, -1)
```

**Output**

`-1`
