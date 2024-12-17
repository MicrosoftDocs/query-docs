---
description: "Learn more about: DateTime.IsInPreviousNHours"
title: "DateTime.IsInPreviousNHours"
ms.subservice: m-source
---
# DateTime.IsInPreviousNHours

## Syntax

<pre>
DateTime.IsInPreviousNHours(<b>dateTime</b> as any, <b>hours</b> as number) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of hours, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.
* `hours`: The number of hours.

## Example 1

Determine if the hour before the current system time is in the previous two hours.

**Usage**

```powerquery-m
DateTime.IsInPreviousNHours(DateTime.FixedLocalNow() - #duration(0, 2, 0, 0), 2)
```

**Output**

`true`
