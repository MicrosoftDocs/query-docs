---
title: "Date.IsInNextNWeeks | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInNextNWeeks

## Syntax

<pre>
Date.IsInNextNWeeks(<b>dateTime</b> as any, <b>weeks</b> as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of weeks, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>weeks</code>: The number of weeks.</li> </ul>

## Example 1
Determine if the week after the current system time is in the next two weeks.

```powerquery-m
Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2)
```

`true`
