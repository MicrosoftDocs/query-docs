---
description: "Learn more about: List.Numbers"
title: "List.Numbers"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# List.Numbers

## Syntax

<pre>
List.Numbers(<b>start</b> as number, <b>count</b> as number, optional <b>increment</b> as nullable number) as list
</pre>
  
## About

Returns a list of numbers given an initial value, count, and optional increment value. The default increment value is 1.

* `start`: The initial value in the list.
* `count`: The number of values to create.
* `increment: _[Optional]_ The value to increment by. If omitted values are incremented by 1.

## Example 1

Generate a list of 10 consecutive numbers starting at 1.

**Usage**

```powerquery-m
List.Numbers(1, 10)
```

**Output**

```powerquery-m
{
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
}
```

## Example 2

Generate a list of 10 numbers starting at 1, with an increment of 2 for each subsequent number.

**Usage**

```powerquery-m
List.Numbers(1, 10, 2)
```

**Output**

```powerquery-m
{
    1,
    3,
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19
}
```
