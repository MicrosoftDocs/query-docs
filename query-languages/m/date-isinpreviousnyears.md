---
title: "Date.IsInPreviousNYears | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNYears

## Syntax

<pre>
Date.IsInPreviousNYears(<b>dateTime</b> as any, <b>years</b> as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the previous number of years, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>years</code>: The number of years.</li> </ul>

## Example 1
Determine if the year before the current system time is in the previous two years.

```powerquery-m
Date.IsInPreviousNYears(Date.AddYears(DateTime.FixedLocalNow(), -1), 2)
```

`true`