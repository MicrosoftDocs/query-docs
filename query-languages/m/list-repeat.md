---
description: "Learn more about: List.Repeat"
title: "List.Repeat"
ms.date: 3/9/2022
---
# List.Repeat

## Syntax

<pre>
List.Repeat(<b>list</b> as list, <b>count</b> as number) as list
</pre>
  
## About

Returns a list that is `count` repetitions of the original list, `list`.

## Example 1

Create a list that has {1, 2} repeated 3 times.

**Usage**

```powerquery-m
List.Repeat({1, 2}, 3)
```

**Output**

`{1, 2, 1, 2, 1, 2}`
