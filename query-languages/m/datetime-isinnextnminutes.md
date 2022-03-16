---
description: "Learn more about: DateTime.IsInNextNMinutes"
title: "DateTime.IsInNextNMinutes | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.IsInNextNMinutes

## Syntax

<pre>
DateTime.IsInNextNMinutes(<b>dateTime</b> as any, <b>minutes</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.
* `minutes`: The number of minutes.

## Example 1

Determine if the minute after the current system time is in the next two minutes.

**Usage**

```powerquery-m
DateTime.IsInNextNMinutes(DateTime.FixedLocalNow() + #duration(0, 0, 2, 0), 2)
```

**Output**

`true`
