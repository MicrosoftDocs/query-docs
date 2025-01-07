---
description: "Learn more about: Date.IsInPreviousNWeeks"
title: "Date.IsInPreviousNWeeks"
ms.subservice: m-source
---
# Date.IsInPreviousNWeeks

## Syntax

<pre>
Date.IsInPreviousNWeeks(<b>dateTime</b> as any, <b>weeks</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of weeks, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `weeks`: The number of weeks.

## Example 1

Determine if the week before the current system time is in the previous two weeks.

**Usage**

```powerquery-m
Date.IsInPreviousNWeeks(Date.AddDays(DateTime.FixedLocalNow(), -7), 2)
```

**Output**

`true`
