---
description: "Learn more about: Date.IsInCurrentWeek"
title: "Date.IsInCurrentWeek"
---
# Date.IsInCurrentWeek

## Syntax

<pre>
Date.IsInCurrentWeek(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About
Indicates whether the given datetime value `dateTime` occurs during the current week, as determined by the current date and time on the system.
* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current week.

**Usage**

```powerquery-m
Date.IsInCurrentWeek(DateTime.FixedLocalNow())
```

**Output**

`true`
