---
description: "Learn more about: Date.IsInPreviousNQuarters"
title: "Date.IsInPreviousNQuarters"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInPreviousNQuarters

## Syntax

<pre>
Date.IsInPreviousNQuarters(<b>dateTime</b> as any, <b>quarters</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `quarters`: The number of quarters.

## Example 1

Determine if the quarter before the current system time is in the previous two quarters.

**Usage**

```powerquery-m
Date.IsInPreviousNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), -1), 2)
```

**Output**

`true`
