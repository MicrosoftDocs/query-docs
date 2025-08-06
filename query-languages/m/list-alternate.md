---
description: "Learn more about: List.Alternate"
title: "List.Alternate"
ms.subservice: m-source
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

Returns a list comprised of all the odd numbered offset elements in a list. Alternates between taking and skipping values from the list `list` depending on the parameters.

* `count`: Specifies number of values that are skipped each time.
* `repeatInterval`: An optional repeat interval to indicate how many values are added in between the skipped values.
* `offset`: An option offset parameter to begin skipping the values at the initial offset.

## Example 1

Create a list from {1..10} that skips the first number.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1)
```

**Output**

`{2, 3, 4, 5, 6, 7, 8, 9, 10}`

## Example 2

Create a list from {1..10} that skips every other number.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1, 1)
```

**Output**

`{2, 4, 6, 8, 10}`

## Example 3

Create a list from {1..10} that starts at 1 and skips every other number.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1, 1, 1)
```

**Output**

`{1, 3, 5, 7, 9}`

## Example 4

Create a list from {1..10} that starts at 1, skips one value, keeps two values, and so on.

**Usage**

```powerquery-m
List.Alternate({1..10}, 1, 2, 1)
```

**Output**

`{1, 3, 4, 6, 7, 9, 10}`
