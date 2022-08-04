---
description: "Learn more about: Date.IsInNextMonth"
title: "Date.IsInNextMonth"
ms.date: 3/22/2022
---
# Date.IsInNextMonth

## Syntax

<pre>
Date.IsInNextMonth(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the next month, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the month after the current system time is in the next month.

**Usage**

```powerquery-m
Date.IsInNextMonth(Date.AddMonths(DateTime.FixedLocalNow(), 1))
```

**Output**

`true`
