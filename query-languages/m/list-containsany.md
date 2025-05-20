---
description: "Learn more about: List.ContainsAny"
title: "List.ContainsAny"
ms.subservice: m-source
---
# List.ContainsAny

## Syntax

<pre>
List.ContainsAny(<b>list</b> as list, <b>values</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>

## About

Indicates whether the list contains any of the values from another list. Returns `true` if the values are found in the list, `false` otherwise.

* `list`: The list to search.
* `values`: The list of values to search for in the first list.
* `equationCriteria`: (Optional) The comparer used to determine if the two values are equal.

## Example 1

Determine if the list {1, 2, 3, 4, 5} contains 3 or 9.

**Usage**

```powerquery-m
List.ContainsAny({1, 2, 3, 4, 5}, {3, 9})
```

**Output**

`true`

## Example 2

Determine if the list {1, 2, 3, 4, 5} contains 6 or 7.

**Usage**

```powerquery-m
List.ContainsAny({1, 2, 3, 4, 5}, {6, 7})
```

**Output**

`false`

## Example 3

Determine if the list contains a horse or an owl, while ignoring case.

**Usage**

```powerquery-m
List.ContainsAny({"dog", "cat", "racoon", "horse", "rabbit"}, {"Horse", "OWL"}, Comparer.OrdinalIgnoreCase)
```

**Output**

`true`

## Example 4

Determine if the list contains a date of either April 8, 2022 or January 12, 2021.

**Usage**

```powerquery-m
let
    Source = {#date(2024, 2, 23), #date(2023, 12, 2), #date(2022, 4, 8), #date(2021, 7, 6)},
    ContainsDates = List.ContainsAny(Source, {Date.From("Apr 8, 2022"), Date.From("Jan 11, 2021")})
in
    ContainsDates
```

**Output**

`true`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
