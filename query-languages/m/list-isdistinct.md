---
description: "Learn more about: List.IsDistinct"
title: "List.IsDistinct"
ms.subservice: m-source
---
# List.IsDistinct

## Syntax

<pre>
List.IsDistinct(<b>list</b> as list, optional <b>equationCriteria</b> as any) as logical
</pre>

## About

Returns a logical value whether there are duplicates in the list `list`; `true` if the list is distinct, `false` if there are duplicate values.

## Example 1

Find if the list {1, 2, 3} is distinct (i.e. no duplicates).

**Usage**

```powerquery-m
List.IsDistinct({1, 2, 3})
```

**Output**

`true`

## Example 2

Find if the list {1, 2, 3, 3} is distinct (i.e. no duplicates).

**Usage**

```powerquery-m
List.IsDistinct({1, 2, 3, 3})
```

**Output**

`false`

## Related content

[Equation criteria](list-functions.md#equation-criteria)
