---
description: "Learn more about: List.ContainsAny"
title: "List.ContainsAny"
---
# List.ContainsAny

## Syntax

<pre>
List.ContainsAny(<b>list</b> as list, <b>values</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>

## About

Indicates whether the list `list` includes any of the values in another list, `values`. Returns true if value is found in the list, false otherwise. An optional equation criteria value, `equationCriteria`, can be specified to control equality testing.

## Example 1

Find out if the list {1, 2, 3, 4, 5} contains 3 or 9.

**Usage**

```powerquery-m
List.ContainsAny({1, 2, 3, 4, 5}, {3, 9})
```

**Output**

`true`

## Example 2

Find out if the list {1, 2, 3, 4, 5} contains 6 or 7.

**Usage**

```powerquery-m
List.ContainsAny({1, 2, 3, 4, 5}, {6, 7})
```

**Output**

`false`
