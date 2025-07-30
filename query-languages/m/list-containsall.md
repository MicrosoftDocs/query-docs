---
description: "Learn more about: List.ContainsAll"
title: "List.ContainsAll"
ms.subservice: m-source
---
# List.ContainsAll

## Syntax

<pre>
List.ContainsAll(<b>list</b> as list, <b>values</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>

## About

Indicates whether the list includes all the values from another list. Returns `true` if all the values are found in the list, `false` otherwise.

* `list`: The list to search.
* `values`: The list of values to search for in the first list.
* `equationCriteria`: (Optional) The comparer used to determine if the two values are equal.

## Example 1

Determine if the list {1, 2, 3, 4, 5} contains 3 and 4.

**Usage**

```powerquery-m
List.ContainsAll({1, 2, 3, 4, 5}, {3, 4})
```

**Output**

`true`

## Example 2

Determine if the list {1, 2, 3, 4, 5} contains 5 and 6.

**Usage**

```powerquery-m
List.ContainsAll({1, 2, 3, 4, 5}, {5, 6})
```

**Output**

`false`

## Example 3

Determine if the list contains a dog and a horse, while ignoring case.

**Usage**

```powerquery-m
List.ContainsAll({"dog", "cat", "racoon", "horse", "rabbit"}, {"DOG", "Horse"}, Comparer.OrdinalIgnoreCase)
```

**Output**

`true`

## Example 4

Determine if the list contains the dates April 8, 2022 and July 6, 2021.

**Usage**

```powerquery-m
let
    Source = {#date(2024, 2, 23), #date(2023, 12, 2), #date(2022, 4, 8), #date(2021, 7, 6)},
    ContainsDates = List.ContainsAll(Source, {#date(2022, 4, 8), #date(2021, 7, 6)})
in
    ContainsDates
```

**Output**

`true`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
