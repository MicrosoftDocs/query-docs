---
title: "Date.IsInPreviousNQuarters | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNQuarters

## About

Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>quarters</code>: The number of quarters.</li> </ul>

## Syntax

<pre>
Date.IsInPreviousNQuarters(<b>dateTime</b> as any, <b>quarters</b> as number) as nullable logical
</pre>

## Example 1
Determine if the quarter before the current system time is in the previous two quarters.

```powerquery-m
Date.IsInPreviousNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), -1), 2)
```

`true`

