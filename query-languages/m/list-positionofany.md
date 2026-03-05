---
description: "Learn more about: List.PositionOfAny"
title: "List.PositionOfAny"
ms.subservice: m-source
ms.topic: reference
---
# List.PositionOfAny

## Syntax

<pre>
List.PositionOfAny(
    <b>list</b> as list,
    <b>values</b> as list,
    optional <b>occurrence</b> as nullable number,
    optional <b>equationCriteria</b> as any
) as any
</pre>
  
## About

Returns the offset at which an item from the specified list of values appears in a list. Returns -1 if no occurrence is found.

* `list`: The list to search.
* `values`: The list of values to find in the original list.
* `occurrence`: (Optional) The specific occurrence to report. This value can be [Occurrence.First](occurrence-type.md), [Occurrence.Last](occurrence-type.md), or [Occurrence.All](occurrence-type.md). If no `occurrence` is specified, `Occurrence.First` is used.
* `equationCriteria`: (Optional) Specifies how equality is determined when comparing values. This parameter can be a key selector function, a comparer function, or a list containing both a key selector and a comparer.

## Example 1

Find the first position in the list {1, 2, 3} at which the value 2 or 3 appears.

**Usage**

```powerquery-m
List.PositionOfAny({1, 2, 3}, {2, 3})
```

**Output**

`1`

## Example 2

Find the position in the list of all instances of dates from either 2022 or 2023.

**Usage**

```powerquery-m
let
    Source = {
        #date(2021, 5, 10),
        #date(2022, 6, 28),
        #date(2023, 7, 15),
        #date(2025, 12, 31),
        #date(2022, 4, 8),
        #date(2024, 3, 20)
    },
    YearList = List.Transform(Source, each Date.Year(_)),
    TargetYear = {2022, 2023},
    FindPositions = List.PositionOfAny(YearList, TargetYear, Occurrence.All)
in
    FindPositions
```

**Output**

`{1, 2, 4}`

## Example 3

Find the position in the list of the last occurrence of either the word dog or cat, ignoring case.

**Usage**

```powerquery-m
let
    Source = List.PositionOfAny(
        {"dog", "cat", "DOG", "pony", "bat", "rabbit", "dOG"}, 
        {"dog", "cat"}, 
        Occurrence.Last, 
        Comparer.OrdinalIgnoreCase
    )
in
    Source
```

**Output**

`6`

## Example 4

Find any position in the list that's within two units of either the number 17 or 28.

**Usage**

```powerquery-m
let
    Source = { 10, 15, 20, 25, 30 },
    Position = List.PositionOfAny(
        Source, 
        {17, 28},
        Occurrence.All, 
        (x, y) => Number.Abs(x - y) <= 2
    )
in
    Position
```

**Output**

`{1, 4}`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
