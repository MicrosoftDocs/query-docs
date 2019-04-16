---
title: "Date.IsInPreviousDay | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousDay

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous day, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current day. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Syntax

<pre>
Date.IsInPreviousDay(<b>dateTime</b> as any) as nullable logical
</pre>

## Example

Determine if the day before the current system time is in the previous day.

```powerquery-m
Date.IsInPreviousDay(Date.AddDays(DateTime.FixedLocalNow(), -1))
```

`true`

