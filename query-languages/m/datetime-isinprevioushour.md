---
description: "Learn more about: DateTime.IsInPreviousHour"
title: "DateTime.IsInPreviousHour"
---
# DateTime.IsInPreviousHour

## Syntax

<pre>
DateTime.IsInPreviousHour(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous hour, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the hour before the current system time is in the previous hour.

**Usage**

```powerquery-m
DateTime.IsInPreviousHour(DateTime.FixedLocalNow() - #duration(0, 1, 0, 0))
```

**Output**

`true`
