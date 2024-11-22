---
description: "Learn more about: List.Median"
title: "List.Median"
---
# List.Median

## Syntax

<pre>
List.Median(<b>list</b> as list, optional <b>comparisonCriteria</b> as any) as any
</pre>

## About

Returns the median item of the list `list`. This function returns `null` if the list contains no non-`null` values. If there is an even number of items, the function chooses the smaller of the two median items unless the list is comprised entirely of datetimes, durations, numbers or times, in which case it returns the average of the two items.

## Example 1

Find the median of the list `{5, 3, 1, 7, 9}`.

**Usage**

```powerquery-m
powerquery-mList.Median({5, 3, 1, 7, 9})
```

**Output**

`5`  

## Related content

[Comparison criteria](list-functions.md#comparison-criteria)
