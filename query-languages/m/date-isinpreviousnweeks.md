---
title: "Date.IsInPreviousNWeeks | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNWeeks

## About

Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of weeks, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>weeks</code>: The number of weeks.</li> </ul>

## Syntax

<pre>
Date.IsInPreviousNWeeks(<b>dateTime</b> as any, <b>weeks</b> as number) as nullable logical
</pre>

## Example 

Determine if the week before the current system time is in the previous two weeks.

```powerquery-m
Date.IsInPreviousNWeeks(Date.AddDays(DateTime.FixedLocalNow(), -7), 2)
```

`true`

