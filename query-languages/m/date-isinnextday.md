---
description: "Learn more about: Date.IsInNextDay"
title: "Date.IsInNextDay"
---
# Date.IsInNextDay

## Syntax

<pre>
Date.IsInNextDay(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next day, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the day after the current system time is in the next day.

**Usage**

```powerquery-m
Date.IsInNextDay(Date.AddDays(DateTime.FixedLocalNow(), 1))
```

**Output**

`true`
