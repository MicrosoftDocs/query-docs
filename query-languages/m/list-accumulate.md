---
title: "List.Accumulate | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

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

```powerquery-m
List.Accumulate({1, 2, 3, 4, 5}, 0, (state, current) => state + current)
```

`15`
