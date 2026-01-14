---
description: "Learn more about: List.RemoveNulls"
title: "List.RemoveNulls"
ms.subservice: m-source
ms.topic: reference
---
# List.RemoveNulls

## Syntax

<pre>
List.RemoveNulls(<b>list</b> as list) as list
</pre>
  
## About

Removes all occurrences of "null" values in the `list`. If there are no 'null' values in the list, the original list is returned.

## Example 1

Remove the "null" values from the list {1, 2, 3, null, 4, 5, null, 6}.

**Usage**

```powerquery-m
List.RemoveNulls({1, 2, 3, null, 4, 5, null, 6})
```

**Output**

`{1, 2, 3, 4, 5, 6}`
