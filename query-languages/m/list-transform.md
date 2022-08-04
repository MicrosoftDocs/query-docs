---
description: "Learn more about: List.Transform"
title: "List.Transform"
ms.date: 3/9/2022
---
# List.Transform

## Syntax

<pre>
List.Transform(<b>list</b> as list, <b>transform</b> as function) as list
</pre>
  
## About

Returns a new list of values by applying the transform function `transform` to the list, `list`.

## Example 1

Add 1 to each value in the list {1, 2}.

**Usage**

```powerquery-m
List.Transform({1, 2}, each _ + 1)
```

**Output**

`{2, 3}`
