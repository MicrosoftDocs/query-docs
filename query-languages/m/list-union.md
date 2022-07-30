---
description: "Learn more about: List.Union"
title: "List.Union"
ms.date: 3/9/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Union

## Syntax

<pre>
List.Union(<b>lists</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About

Takes a list of lists `lists`, unions the items in the individual lists and returns them in the output list. As a result, the returned list contains all items in any input lists. This operation maintains traditional bag semantics, so duplicate values are matched as part of the Union. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Create a union of the list {1..5}, {2..6}, {3..7}.

**Usage**

```powerquery-m
List.Union({{1..5}, {2..6}, {3..7}})
```

**Output**

`{1, 2, 3, 4, 5, 6, 7}`
