---
title: "Date.IsInPreviousNMonths | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNMonths

## Syntax

<pre>
Date.IsInPreviousNMonths(**dateTime** as any, **months** as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the previous number of months, as determined by the current date and time on the system. 
* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `months`: The number of months.

## Example 1
Determine if the month before the current system time is in the previous two months.

```powerquery-m
Date.IsInPreviousNMonths(Date.AddMonths(DateTime.FixedLocalNow(), -1), 2)
```

`true`

