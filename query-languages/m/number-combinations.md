---
description: "Learn more about: Number.Combinations"
title: "Number.Combinations"
ms.date: 10/10/2022
---
# Number.Combinations

## Syntax

<pre>
Number.Combinations(<b>setSize</b> as nullable number, <b>combinationSize</b> as nullable number) as nullable number
</pre>

## About

Returns the number of unique combinations from a list of items, `setSize` with specified combination size, `combinationSize`.

* `setSize`: The number of items in the list.
* `combinationSize`: The number of items in each combination.

## Example 1

Find the number of combinations from a total of 5 items when each combination is a group of 3.

**Usage**

```powerquery-m
Number.Combinations(5, 3)
```

**Output**

`10`
