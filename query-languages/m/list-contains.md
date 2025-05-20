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

Indicates whether the list contains the specified value. Returns `true` if the value is found in the list, `false` otherwise.

* `list`: The list to search.
* `value`: The value to search for in the list.
* `equationCriteria`: (Optional) The comparer used to determine if the two values are equal.

## Example 1

Determine if the list {1, 2, 3, 4, 5} contains 3.

**Usage**

```powerquery-m
List.Contains({1, 2, 3, 4, 5}, 3)
```

**Output**

`true`

## Example 2

Determine if the list {1, 2, 3, 4, 5} contains 6.

**Usage**

```powerquery-m
List.Contains({1, 2, 3, 4, 5}, 6)
```

**Output**

`false`

## Example 3

Ignoring case, determine if the list contains "rhubarb".

**Usage**

```powerquery-m
List.Contains({"Pears", "Bananas", "Rhubarb", "Peaches"},
    "rhubarb",
    Comparer.OrdinalIgnoreCase
)
```

**Output**

`true`

## Example 4

Determine if the list contains a date April 8, 2022.

**Usage**

```powerquery-m
let
    Source = {#date(2024, 2, 23), #date(2023, 12, 2), #date(2022, 4, 8), #date(2021, 7, 6)},
    ContainsDate = List.Contains(Source, Date.From("4/8/2022"))
in
    ContainsDate
```

**Output

`true`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
