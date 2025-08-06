---
description: "Learn more about: List.DateTimes"
title: "List.DateTimes"
ms.subservice: m-source
---
# List.DateTimes

## Syntax

<pre>
List.DateTimes(
    <b>start</b> as datetime,
    <b>count</b> as number,
    <b>step</b> as duration
) as list
</pre>

## About

Returns a list of `datetime` values of size `count`, starting at `start`. The given increment, `step`, is a `duration` value that is added to every value.

## Example

Create a list of 10 values starting from 5 minutes before New Year's Day (#datetime(2011, 12, 31, 23, 55, 0)) incrementing by 1 minute (#duration(0, 0, 1, 0)).

**Usage**

```powerquery-m
List.DateTimes(#datetime(2011, 12, 31, 23, 55, 0), 10, #duration(0, 0, 1, 0))
```

**Output**

```powerquery-m
{
    #datetime(2011, 12, 31, 23, 55, 0),
    #datetime(2011, 12, 31, 23, 56, 0),
    #datetime(2011, 12, 31, 23, 57, 0),
    #datetime(2011, 12, 31, 23, 58, 0),
    #datetime(2011, 12, 31, 23, 59, 0),
    #datetime(2012, 1, 1, 0, 0, 0),
    #datetime(2012, 1, 1, 0, 1, 0),
    #datetime(2012, 1, 1, 0, 2, 0),
    #datetime(2012, 1, 1, 0, 3, 0),
    #datetime(2012, 1, 1, 0, 4, 0)
}
```
