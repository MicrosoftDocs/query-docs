---
description: "Learn more about: DateTime.IsInPreviousNSeconds"
title: "DateTime.IsInPreviousNSeconds"
ms.subservice: m-source
ms.topic: reference
---
# DateTime.IsInPreviousNSeconds

## Syntax

<pre>
DateTime.IsInPreviousNSeconds(<b>dateTime</b> as any, <b>seconds</b> as number) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of seconds, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second.

* `dateTime`: A `datetime`>, or `datetimezone` value to be evaluated.
* `seconds`: The number of seconds.

## Example 1

Determine if the second before the current system time is in the previous two seconds.

**Usage**

```powerquery-m
DateTime.IsInPreviousNSeconds(DateTime.FixedLocalNow() - #duration(0, 0, 0, 2), 2)
```

**Output**

`true`
