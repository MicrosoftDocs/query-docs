---
title: "Date.IsInNextNMonths | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNMonths

## Syntax

<pre>
Date.IsInNextNMonths(**dateTime** as any, **months** as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of months, as determined by the current date and time on the system. 
- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
- `months`: The number of months.

## Example 
Determine if the month after the current system time is in the next two months.

```powerquery-m
Date.IsInNextNMonths(Date.AddMonths(DateTime.FixedLocalNow(), 1), 2)
```

`true`

