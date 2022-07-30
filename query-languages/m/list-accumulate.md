---
description: "Learn more about: List.Accumulate"
title: "List.Accumulate | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Accumulate

## Syntax

<pre>
List.Accumulate(<b>list</b> as list, <b>seed</b> as any, <b>accumulator</b> as function) as any
</pre>
  
## About

Accumulates a summary value from the items in the list `list`, using `accumulator`. An optional seed parameter, `seed`, may be set.

## Example 1

Accumulates the summary value from the items in the list {1, 2, 3, 4, 5} using ((state, current) => state + current ).

**Usage**

```powerquery-m
List.Accumulate({1, 2, 3, 4, 5}, 0, (state, current) => state + current)
```

**Output**

`15`
