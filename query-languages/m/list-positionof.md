---
description: "Learn more about: List.PositionOf"
title: "List.PositionOf"
ms.subservice: m-source
---
# List.PositionOf

## Syntax

<pre>
List.PositionOf(
    <b>list</b> as list,
    <b>value</b> as any,
    optional <b>occurrence</b> as nullable number,
    optional <b>equationCriteria</b> as any
) as any
</pre>
  
## About

Returns the offset at which the specified value appears in a list. Returns -1 if the value doesn't appear.

* `list`: The list to search.
* `value`: The value to find in the list.
* `occurrence`: (Optional) The specific occurrence to report. This value can be [Occurrence.First](occurrence-type.md), [Occurrence.Last](occurrence-type.md), or [Occurrence.All](occurrence-type.md).
* `equationCriteria`: (Optional) Specifies how equality is determined when comparing values. This parameter can be a key selector function, a comparer function, or a list containing both a key selector and a comparer.

## Example 1

Find the position in the list {1, 2, 3} at which the value 3 appears.

**Usage**

```powerquery-m
List.PositionOf({1, 2, 3}, 3)
```

**Output**

`2`

## Example 2

Find the position in the list of all instances of dates from 2022.

**Usage**

```powerquery-m
let
    Source = {
        #date(2021, 5, 10),
        #date(2022, 6, 28),
        #date(2023, 7, 15),
        #date(2022, 12, 31),
        #date(2022, 4, 8),
        #date(2024, 3, 20)
    },
    YearList = List.Transform(Source, each Date.Year(_)),
    TargetYear = 2022,
    FindPositions = List.PositionOf(YearList, TargetYear, Occurrence.All)
in
    FindPositions
```

**Output**

`{1, 3, 4}`

## Example 3

Find the position in the list of the last occurrence of the word dog, ignoring case.

**Usage**

```powerquery-m
let
    Source = List.PositionOf(
        {"dog", "cat", "DOG", "pony", "bat", "rabbit", "dOG"}, 
        "dog", 
        Occurrence.Last, 
        Comparer.OrdinalIgnoreCase
    )
in
    Source
```

**Output**

`6`

## Example 4

Find the position in the list that is within two units of the number 28.

**Usage**

```powerquery-m
let
    Source = { 10, 15, 20, 25, 30 },
    Position = List.PositionOf(
        Source, 
        28,
        Occurrence.First, 
        (x, y) => Number.Abs(x - y) <= 2
    )
in
    Position
```

**Output**

`4`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
