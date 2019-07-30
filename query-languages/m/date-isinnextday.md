---
title: "Date.IsInNextDay | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextDay

## Syntax

<pre>
Date.IsInNextDay(<b>dateTime</b> as any) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next day, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the day after the current system time is in the next day.

```powerquery-m
Date.IsInNextDay(Date.AddDays(DateTime.FixedLocalNow(), 1))
```

`true`
