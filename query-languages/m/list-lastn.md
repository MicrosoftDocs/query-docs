---
description: "Learn more about: List.LastN"
title: "List.LastN"
ms.subservice: m-source
---
# List.LastN

## Syntax

<pre>
List.LastN(<b>list</b> as list, optional <b>countOrCondition</b> as any) as any
</pre>

## About

Returns a list of the last item or items in the specified list.

* `list`: The list to examine. If the list is empty, an empty list is returned.
* `countOrCondition`: (Optional) Supports gathering multiple items or filtering items. Although this parameter is listed as optional, an error occurs if this value isn't provided or is `null`. This parameter can be specified in two ways:
  * If a number is specified, up to that many items are returned.
  * If a condition is specified, all items are returned that meet the condition, starting at the end of the list. Once an item fails the condition, no further items are considered.

## Example 1

Find the last value in the list {3, 4, 5, -1, 7, 8, 2}.

**Usage**

```powerquery-m
List.LastN({3, 4, 5, -1, 7, 8, 2}, 1)
```

**Output**

`{2}`

## Example 2

Find the last values in the list {3, 4, 5, -1, 7, 8, 2} that are greater than 0.

**Usage**

```powerquery-m
List.LastN({3, 4, 5, -1, 7, 8, 2}, each _ > 0)
```

**Output**

`{7, 8, 2}`
