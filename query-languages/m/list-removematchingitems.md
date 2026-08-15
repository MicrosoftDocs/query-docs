---
description: "Learn more about: List.RemoveMatchingItems"
title: "List.RemoveMatchingItems"
ms.subservice: m-source
ms.topic: reference
---

# List.RemoveMatchingItems

## Syntax

<pre>
List.RemoveMatchingItems(
    <b>list1</b> as list,
    <b>list2</b> as list,
    optional <b>equationCriteria</b> as any
) as list
</pre>

## About

Removes all occurrences of the given values in `list2` from the list `list1`. If the values in `list2` don't exist in `list1`, the original list is returned. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example

Remove the numbers 1 and 5 from the list.

**Usage**

```powerquery-m
List.RemoveMatchingItems({1, 2, 3, 4, 5, 5}, {1, 5})
```

**Output**

`{2, 3, 4}`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
