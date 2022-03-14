---
description: "Learn more about: Date.IsInPreviousNDays"
title: "Date.IsInPreviousNDays | Microsoft Docs"
ms.date: 3/22/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInPreviousNDays

## Syntax

<pre>
Date.IsInPreviousNDays(<b>dateTime</b> as any, <b>days</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of days, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `days: The number of days.

## Example 1

Determine if the day before the current system time is in the previous two days.

**Usage**

```powerquery-m
Date.IsInPreviousNDays(Date.AddDays(DateTime.FixedLocalNow(), -1), 2)
```

**Output**

`true`
