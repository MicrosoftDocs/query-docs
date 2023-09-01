---
description: "Learn more about: Date.IsInPreviousWeek"
title: "Date.IsInPreviousWeek"
---
# Date.IsInPreviousWeek

## Syntax

<pre>
Date.IsInPreviousWeek(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous week, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the week before the current system time is in the previous week.

**Usage**

```powerquery-m
Date.IsInPreviousWeek(Date.AddDays(DateTime.FixedLocalNow(), -7))
```

**Output**

`true`
