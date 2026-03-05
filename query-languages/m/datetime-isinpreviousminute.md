---
description: "Learn more about: DateTime.IsInPreviousMinute"
title: "DateTime.IsInPreviousMinute"
ms.subservice: m-source
ms.topic: reference
---
# DateTime.IsInPreviousMinute

## Syntax

<pre>
DateTime.IsInPreviousMinute(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous minute, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the minute before the current system time is in the previous minute.

**Usage**

```powerquery-m
DateTime.IsInPreviousMinute(DateTime.FixedLocalNow() - #duration(0, 0, 1, 0))
```

**Output**

`true`
