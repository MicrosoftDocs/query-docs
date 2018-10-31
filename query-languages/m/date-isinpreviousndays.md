---
title: "Date.IsInPreviousNDays | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNDays

## Syntax

<pre>
Date.IsInPreviousNDays(**dateTime** as any, **days** as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the previous number of days, as determined by the current date and time on the system. 
* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
* `days`: The number of days.

## Example 1
Determine if the day before the current system time is in the previous two days.

```powerquery-m
Date.IsInPreviousNDays(Date.AddDays(DateTime.FixedLocalNow(), -1), 2)
```

`true`

