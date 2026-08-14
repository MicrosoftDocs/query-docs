---
description: "Learn more about: List.ReplaceMatchingItems"
title: "List.ReplaceMatchingItems"
ms.subservice: m-source
ms.topic: reference
---

# List.ReplaceMatchingItems

## Syntax

<pre>
List.ReplaceMatchingItems(
    <b>list</b> as list,
    <b>replacements</b> as list,
    optional <b>equationCriteria</b> as any
) as list
</pre>

## About

Performs the given replacements to the list `list`. A replacement operation `replacements` consists of a list of two values, the old value and new value, provided in a list. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example

Replace the numbers 5 and 1 in the list with their negative equivalents.

**Usage**

```powerquery-m
List.ReplaceMatchingItems({1, 2, 3, 4, 5}, {{5, -5}, {1, -1}})
```

**Output**

`{-1, 2, 3, 4, -5}`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
