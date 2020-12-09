---
title: "Date.IsInNextNDays | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInNextNDays

## Syntax

<pre>
Date.IsInNextNDays(<b>dateTime</b> as any, <b>days</b> as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of days, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>days</code>: The number of days.</li> </ul>

## Example 1
Determine if the day after the current system time is in the next two days.

```powerquery-m
Date.IsInNextNDays(Date.AddDays(DateTime.FixedLocalNow(), 1), 2)
```

`true`
