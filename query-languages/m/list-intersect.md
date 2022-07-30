---
description: "Learn more about: List.Intersect"
title: "List.Intersect | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Intersect

## Syntax

<pre>
List.Intersect(<b>lists</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About

Returns the intersection of the list values found in the input list `lists`. An optional parameter, `equationCriteria`, can be specified.

## Example 1

Find the intersection of the lists {1..5}, {2..6}, {3..7}.

**Usage**

```powerquery-m
List.Intersect({{1..5}, {2..6}, {3..7}})
```

**Output**

`{3, 4, 5}`
