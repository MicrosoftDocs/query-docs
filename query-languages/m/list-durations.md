---
description: "Learn more about: List.Durations"
title: "List.Durations"
---
# List.Durations

## Syntax

<pre>
List.Durations(<b>start</b> as duration, <b>count</b> as number, <b>step</b> as duration) as list
</pre>

## About

Returns a list of `count` `duration` values, starting at `start` and incremented by the given `duration` `step`.

## Example 1

Create a list of 5 values starting 1 hour and incrementing by an hour.

**Usage**

```powerquery-m
List.Durations(#duration(0, 1, 0, 0), 5, #duration(0, 1, 0, 0))
```

**Output**

```powerquery-m
{
    #duration(0, 1, 0, 0),
    #duration(0, 2, 0, 0),
    #duration(0, 3, 0, 0),
    #duration(0, 4, 0, 0),
    #duration(0, 5, 0, 0)
}
```
