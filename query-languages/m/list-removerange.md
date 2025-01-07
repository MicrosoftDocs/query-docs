---
description: "Learn more about: List.RemoveRange"
title: "List.RemoveRange"
ms.subservice: m-source
---
# List.RemoveRange

## Syntax

<pre>
List.RemoveRange(<b>list</b> as list, <b>index</b> as number, optional <b>count</b> as nullable number) as list
</pre>
  
## About

Removes `count` values in the `list` starting at the specified position, `index`.

## Example 1

Remove 3 values in the list {1, 2, 3, 4, -6, -2, -1, 5} starting at index 4.

**Usage**

```powerquery-m
List.RemoveRange({1, 2, 3, 4, -6, -2, -1, 5}, 4, 3)
```

**Output**

`{1, 2, 3, 4, 5}`
