---
description: "Learn more about: Date.IsInNextWeek"
title: "Date.IsInNextWeek"
ms.subservice: m-source
---
# Date.IsInNextWeek

## Syntax

<pre>
Date.IsInNextWeek(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next week, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the week after the current system time is in the next week.

**Usage**

```powerquery-m
Date.IsInNextWeek(Date.AddDays(DateTime.FixedLocalNow(), 7))
```

**Output**

`true`
