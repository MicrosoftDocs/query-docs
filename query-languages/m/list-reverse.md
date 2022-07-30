---
description: "Learn more about: List.Reverse"
title: "List.Reverse"
ms.date: 3/9/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Reverse

## Syntax

<pre>
List.Reverse(<b>list</b> as list) as list
</pre>
  
## About

Returns a list with the values in the list `list` in reversed order.

## Example 1

Create a list from {1..10} in reverse order.

**Usage**

```powerquery-m
List.Reverse({1..10})
```

**Output**

`{10, 9, 8, 7, 6, 5, 4, 3, 2, 1}`
