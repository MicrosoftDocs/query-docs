---
description: "Learn more about: List.InsertRange"
title: "List.InsertRange"
ms.subservice: m-source
---
# List.InsertRange

## Syntax

<pre>
List.InsertRange(
    <b>list</b> as list,
    <b>index</b> as number,
    <b>values</b> as list
) as list
</pre>

## About

Returns a new list produced by inserting the values in `values` into `list` at `index`. The first position in the list is at index 0.

* `list`: The target list where values are to be inserted.
* `index`: The index of the target list(`list`) where the values are to be inserted. The first position in the list is at index 0.
* `values`: The list of values which are to be inserted into `list`.

## Example 1

Insert the list ({3, 4}) into the target list ({1, 2, 5}) at index 2.

**Usage**

```powerquery-m
List.InsertRange({1, 2, 5}, 2, {3, 4})
```

**Output**

```powerquery-m
{
    1,
    2,
    3,
    4,
    5
}
```

## Example 2

Insert a list with a nested list ({1, {1.1, 1.2}}) into a target list ({2, 3, 4}) at index 0.

**Usage**

```powerquery-m
List.InsertRange({2, 3, 4}, 0, {1, {1.1, 1.2}})
```

**Output**

```powerquery-m
{
    1,
    {
        1.1,
        1.2
    },
    2,
    3,
    4
}
```
