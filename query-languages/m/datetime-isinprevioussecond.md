---
description: "Learn more about: DateTime.IsInPreviousSecond"
title: "DateTime.IsInPreviousSecond"
ms.subservice: m-source
---
# DateTime.IsInPreviousSecond

## Syntax

<pre>
DateTime.IsInPreviousSecond(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous second, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the second before the current system time is in the previous second.

**Usage**

```powerquery-m
DateTime.IsInPreviousSecond(DateTime.FixedLocalNow() - #duration(0, 0, 0, 1))
```

**Output**

`true`
