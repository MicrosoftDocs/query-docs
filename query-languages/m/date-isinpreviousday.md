---
description: "Learn more about: Date.IsInPreviousDay"
title: "Date.IsInPreviousDay"
ms.date: 3/11/2022
---
# Date.IsInPreviousDay

## Syntax

<pre>
Date.IsInPreviousDay(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous day, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the day before the current system time is in the previous day.

**Usage**

```powerquery-m
Date.IsInPreviousDay(Date.AddDays(DateTime.FixedLocalNow(), -1))
```

**Output**

`true`
