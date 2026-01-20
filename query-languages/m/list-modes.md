---
description: "Learn more about: List.Modes"
title: "List.Modes"
ms.subservice: m-source
ms.topic: reference
---
# List.Modes

## Syntax

<pre>
List.Modes(<b>list</b> as list, optional <b>equationCriteria</b> as any) as list
</pre>
  
## About

Returns the items that appear most frequently in `list`. If the list is empty an error is raised. If multiple items appear with the same maximum frequency, all of them are returned. An optional comparison criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Find the items that appears most frequently in the list `{"A", 1, 2, 3, 3, 4, 5, 5}`.

**Usage**

```powerquery-m
List.Modes({"A", 1, 2, 3, 3, 4, 5, 5})
```

**Output**

`{3, 5}`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
