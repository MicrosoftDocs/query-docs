---
description: "Learn more about: Date.IsInNextNWeeks"
title: "Date.IsInNextNWeeks"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInNextNWeeks

## Syntax

<pre>
Date.IsInNextNWeeks(<b>dateTime</b> as any, <b>weeks</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of weeks, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `weeks`: The number of weeks.

## Example 1

Determine if the week after the current system time is in the next two weeks.

**Usage**

```powerquery-m
Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2)
```

**Output**

`true`
