---
description: "Learn more about: Time.Second"
title: "Time.Second"
ms.subservice: m-source
---
# Time.Second

## Syntax

<pre>
Time.Second(<b>dateTime</b> as any) as nullable number
</pre>

## About

Returns the second component of the provided `time`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1

Find the second value from a datetime value.

**Usage**

```powerquery-m
Time.Second(#datetime(2011, 12, 31, 9, 15, 36.5))
```

**Output**

`36.5`
