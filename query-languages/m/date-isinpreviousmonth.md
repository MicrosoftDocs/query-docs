---
description: "Learn more about: Date.IsInPreviousMonth"
title: "Date.IsInPreviousMonth"
ms.subservice: m-source
---
# Date.IsInPreviousMonth

## Syntax

<pre>
Date.IsInPreviousMonth(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the previous month, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the month before the current system time is in the previous month.

**Usage**

```powerquery-m
Date.IsInPreviousMonth(Date.AddMonths(DateTime.FixedLocalNow(), -1))
```

**Output**

`true`
