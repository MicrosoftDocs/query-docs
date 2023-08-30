---
description: "Learn more about: List.PositionOf"
title: "List.PositionOf"
---
# List.PositionOf

## Syntax

<pre>
List.PositionOf(<b>list</b> as list, <b>value</b> as any, optional <b>occurrence</b> as nullable number, optional <b>equationCriteria</b> as any) as any
</pre>
  
## About

Returns the offset at which the value `value` appears in the list `list`. Returns -1 if the value doesn't appear. An optional occurrence parameter `occurrence` can be specified.

* `occurrence`: The maximum number of occurrences to report.

## Example 1

Find the position in the list {1, 2, 3} at which the value 3 appears.

**Usage**

```powerquery-m
List.PositionOf({1, 2, 3}, 3)
```

**Output**

`2`
