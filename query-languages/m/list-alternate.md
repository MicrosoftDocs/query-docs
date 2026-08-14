---
description: "Learn more about: List.Alternate"
title: "List.Alternate"
ms.subservice: m-source
ms.topic: reference
---

# List.Alternate

## Syntax

<pre>
List.Alternate(
    <b>list</b> as list,
    <b>count</b> as number,
    optional <b>repeatInterval</b> as nullable number,
    optional <b>offset</b> as nullable number
) as list
</pre>

## About

Returns a new list by alternatively keeping and skipping the items in `list`. The function keeps `offset` initial items, then repeatedly skips `count` items and keeps `repeatInterval` items.

* `count`: The number of items to skip each time.
* `repeatInterval`: An optional number of items to keep after each skip. If this value isn't provided, then all of the items after the initial skip are kept.
* `offset`: An optional number of items to keep before the repeating skip/keep pattern begins. Defaults to zero.

## Example 1

Create a list that skips the first number.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1)
```

**Output**

`{2, 3, 4, 5, 6, 7, 8, 9, 10}`

## Example 2

Create a list that skips every other number.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1, 1)
```

**Output**

`{2, 4, 6, 8, 10}`

## Example 3

Create a list that starts at 1 and skips every other number.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1, 1, 1)
```

**Output**

`{1, 3, 5, 7, 9}`

## Example 4

Create a list that starts at 1, skips one value, keeps two values, and so on.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1, 2, 1)
```

**Output**

`{1, 3, 4, 6, 7, 9, 10}`
