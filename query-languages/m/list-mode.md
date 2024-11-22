---
description: "Learn more about: List.Mode"
title: "List.Mode"
---
# List.Mode

## Syntax

<pre>
List.Mode(<b>list</b> as list, optional <b>equationCriteria</b> as any) as any
</pre>
  
## About

Returns the item that appears most frequently in `list`. If the list is empty an exception is thrown. If multiple items appear with the same maximum frequency, the last one is chosen. An optional comparison criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Find the item that appears most frequently in the list `{"A", 1, 2, 3, 3, 4, 5}`.

**Usage**

```powerquery-m
List.Mode({"A", 1, 2, 3, 3, 4, 5})
```

**Output**

`3`

## Example 2

Find the item that appears most frequently in the list `{"A", 1, 2, 3, 3, 4, 5, 5}`.

**Usage**

```powerquery-m
List.Mode({"A", 1, 2, 3, 3, 4, 5, 5})
```

**Output**

`5`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
