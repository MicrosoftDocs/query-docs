---
description: "Learn more about: List.Skip"
title: "List.Skip"
ms.subservice: m-source
ms.topic: reference
---

# List.Skip

## Syntax

<pre>
List.Skip(<b>list</b> as list, optional <b>countOrCondition</b> as any) as list
</pre>

## About

Returns a list that skips the first element of list `list`. If `list` is an empty list an empty list is returned. This function takes an optional parameter, `countOrCondition`, to support skipping multiple values as listed below.

* If a number is specified, up to that many items are skipped.
* If a condition is specified, any consecutive matching items at the start of `list` are skipped.
* If this parameter is null, the default behavior is observed.

## Example 1

Skip the first three numbers in the list.

**Usage**

```powerquery-m
List.Skip({1, 2, 3, 4, 5}, 3)
```

**Output**

`{4, 5}`

## Example 2

Skip the leading numbers in the list as long as they're greater than 3.

**Usage**

```powerquery-m
List.Skip({5, 4, 2, 6, 1}, each _ > 3)
```

**Output**

`{2, 6, 1}`
