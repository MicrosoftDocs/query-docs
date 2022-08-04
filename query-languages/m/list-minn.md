---
description: "Learn more about: List.MinN"
title: "List.MinN"
ms.date: 3/16/2022
---
# List.MinN

## Syntax

<pre>
List.MinN(<b>list</b> as list, <b>countOrCondition</b> as any, optional <b>comparisonCriteria</b> as any, optional <b>includeNulls</b> as nullable logical) as list
</pre>
  
## About

Returns the minimum value(s) in the list, `list`. The parameter, `countOrCondition`, specifies the number of values to return or a filtering condition. The optional parameter, `comparisonCriteria`, specifies how to compare values in the list.

* `list`: The list of values.
* `countOrCondition`: If a number is specified, a list of up to `countOrCondition` items in ascending order is returned. If a condition is specified, a list of items that initially meet the condition is returned. Once an item fails the condition, no further items are considered. If this parameter is null, the single smallest value in the list is returned.
* `comparisonCriteria`: _[Optional]_ An optional `comparisonCriteria` value can be specified to determine how to compare the items in the list. If this parameter is null, the default comparer is used.

## Example 1

Find the 5 smallest values in the list `{3, 4, 5, -1, 7, 8, 2}`.

**Usage**

```powerquery-m
List.MinN({3, 4, 5, -1, 7, 8, 2}, 5)
```

**Output**

`{-1, 2, 3, 4, 5}`
