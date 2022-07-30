---
description: "Learn more about: DateTime.IsInPreviousNMinutes"
title: "DateTime.IsInPreviousNMinutes | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# DateTime.IsInPreviousNMinutes

## Syntax

<pre>
DateTime.IsInPreviousNMinutes(<b>dateTime</b> as any, <b>minutes</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the previous number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.
* `minutes: The number of minutes.

## Example 1

Determine if the minute before the current system time is in the previous two minutes.

**Usage**

```powerquery-m
DateTime.IsInPreviousNMinutes(DateTime.FixedLocalNow() - #duration(0, 0, 2, 0), 2)
```

**Output**

`true`
