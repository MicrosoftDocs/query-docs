---
description: "Learn more about: Date.IsInPreviousNMonths"
title: "Date.IsInPreviousNMonths"
ms.subservice: m-source
ms.topic: reference
---
# Date.IsInPreviousNMonths

## Syntax

<pre>
Date.IsInPreviousNMonths(<b>dateTime</b> as any, <b>months</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of months, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `months`: The number of months.

## Example 1

Determine if the month before the current system time is in the previous two months.

**Usage**

```powerquery-m
Date.IsInPreviousNMonths(Date.AddMonths(DateTime.FixedLocalNow(), -1), 2)
```

**Output**

`true`
