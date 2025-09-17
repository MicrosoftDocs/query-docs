---
description: "Learn more about: List.MaxN"
title: "List.MaxN"
ms.subservice: m-source
---
# List.MaxN

## Syntax

<pre>
List.MaxN(
    <b>list</b> as list,
    <b>countOrCondition</b> as any,
    optional <b>comparisonCriteria</b> as any,
    optional <b>includeNulls</b> as nullable logical
) as list
</pre>
  
## About

Returns the maximum value(s) in the specified list. After the rows are sorted, optional parameters can be specified to further filter the result.

* `list`: The list of values.
* `countOrCondition`: Specifies the number of values to return or a filtering condition. If a number is specified, a list of up to `countOrCondition` items in ascending order is returned. If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered.
* `comparisonCriteria`: (Optional) Specifies how to compare items in the list. If this parameter is `null`, the default comparer is used.

## Example 1

Find the top 5 values in the specified list

**Usage**

```powerquery-m
List.MaxN({3, 4, 5, -1, 7, 8, 2}, 5)
```

**Output**

`{8, 7, 5, 4, 3}`

## Example 2

Find the word with the maximum number of characters over 3.

**Usage**

```powerquery-m
let
    Source = List.MaxN({"boy", "dog", "pony", "cat", "rabbit", "bat"}, each Text.Length(_) > 3)
in
    Source
```

**Output**

`{"rabbit", "pony"}`

## Example 3

Find the three most recent dates from a list of German dates.

**Usage**

```powerquery-m
let
    Source = {"12.02.2024", "15.05.2025", "10.10.2021", "16.01.2025", "30.12.2022"},
    MaxDate = List.MaxN(Source, 3, each Date.FromText(_, [Culture = "de-DE"]))
in
    MaxDate
```

**Output**

```powerquery-m
{
    "15.05.2025",
    "16.01.2025",
    "12.02.2024"
}
```

## Related content

[Comparison criteria](list-functions.md#comparison-criteria)
