---
description: "Learn more about: DateTime.IsInNextMinute"
title: "DateTime.IsInNextMinute"
---
# DateTime.IsInNextMinute

## Syntax

<pre>
DateTime.IsInNextMinute(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next minute, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the minute after the current system time is in the next minute.

**Usage**

```powerquery-m
DateTime.IsInNextMinute(DateTime.FixedLocalNow() + #duration(0, 0, 1, 0))
```

**Output**

`true`
