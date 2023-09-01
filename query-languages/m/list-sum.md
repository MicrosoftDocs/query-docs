---
description: "Learn more about: List.Sum"
title: "List.Sum"
---
# List.Sum

## Syntax

<pre>
List.Sum(<b>list</b> as list, optional <b>precision</b> as nullable number) as any
</pre>
  
## About

Returns the sum of the non-null values in the list, `list`. Returns null if there are no non-null values in the list.

## Example 1

Find the sum of the numbers in the list `{1, 2, 3}`.

**Usage**

```powerquery-m
List.Sum({1, 2, 3})
```

**Output**

`6`
