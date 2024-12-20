---
description: "Learn more about: List.Contains"
title: "List.Contains"
ms.subservice: m-source
---
# List.Contains

## Syntax

<pre>
List.Contains(<b>list</b> as list, <b>value</b> as any, optional <b>equationCriteria</b> as any) as logical 
</pre>

## About

Indicates whether the list `list` contains the value `value`. Returns true if value is found in the list, false otherwise. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Find if the list {1, 2, 3, 4, 5} contains 3.

**Usage**

```powerquery-m
List.Contains({1, 2, 3, 4, 5}, 3)
```

**Output**

`true`

## Example 2

Find if the list {1, 2, 3, 4, 5} contains 6.

**Usage**

```powerquery-m
List.Contains({1, 2, 3, 4, 5}, 6)
```

**Output**

`false`

## Example 3

Ignoring case, find if the list contains "rhubarb".

**Usage**

```powerquery-m
List.Contains({"Pears", "Bananas", "Rhubarb", "Peaches"},
    "rhubarb",
    Comparer.OrdinalIgnoreCase
)
```

**Output**

`true`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
