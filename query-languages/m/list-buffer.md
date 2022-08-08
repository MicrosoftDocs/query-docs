---
description: "Learn more about: List.Buffer"
title: "List.Buffer"
ms.date: 3/8/2022
---
# List.Buffer

## Syntax

<pre>
List.Buffer(<b>list</b> as list) as list
</pre>
  
## About

Buffers the list `list` in memory. The result of this call is a stable list.

## Example 1

Create a stable copy of the list {1..10}.

**Usage**

```powerquery-m
List.Buffer({1..10})
```

**Output**

`{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}`
