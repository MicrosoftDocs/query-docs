---
description: "Learn more about: DateTime.IsInNextHour"
title: "DateTime.IsInNextHour"
---
# DateTime.IsInNextHour

## Syntax

<pre>
DateTime.IsInNextHour(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next hour, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the hour after the current system time is in the next hour.

**Usage**

```powerquery-m
DateTime.IsInNextHour(DateTime.FixedLocalNow() + #duration(0, 1, 0, 0))
```

**Output**

`true`
