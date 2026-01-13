---
description: "Learn more about: Date.IsInPreviousYear"
title: "Date.IsInPreviousYear"
ms.subservice: m-source
ms.topic: reference
---
# Date.IsInPreviousYear

## Syntax

<pre>
Date.IsInPreviousYear(<b>dateTime</b> as any) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous year, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the year before the current system time is in the previous year.

**Usage**

```powerquery-m
Date.IsInPreviousYear(Date.AddYears(DateTime.FixedLocalNow(), -1))
```

**Output**

`true`
