---
description: "Learn more about: Date.IsInNextNMonths"
title: "Date.IsInNextNMonths | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInNextNMonths

<pre>
Date.IsInNextNMonths(<b>dateTime</b> as any, <b>months</b> as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of months, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>months</code>: The number of months.</li> </ul>

## Example 1
Determine if the month after the current system time is in the next two months.

```powerquery-m
Date.IsInNextNMonths(Date.AddMonths(DateTime.FixedLocalNow(), 1), 2)
```

`true`
