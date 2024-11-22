---
description: "Learn more about: List.Distinct"
title: "List.Distinct"
---
# List.Distinct

## Syntax

<pre>
List.Distinct(<b>list</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>

## About

Returns a list that contains all the values in list `list` with duplicates removed. If the list is empty, the result is an empty list.

## Example 1

Remove the duplicates from the list {1, 1, 2, 3, 3, 3}.

**Usage**

```powerquery-m
List.Distinct({1, 1, 2, 3, 3, 3})
```

**Output**

`{1, 2, 3}`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
