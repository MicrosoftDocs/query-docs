---
title: "Date.IsInNextNWeeks | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNWeeks

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of weeks, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week.

- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
- `weeks`: The number of weeks.

## Syntax

<pre>
Date.IsInNextNWeeks(**dateTime** as any, **weeks** as number) as nullable logical
</pre>

## Example

Determine if the week after the current system time is in the next two weeks.

```powerquery-m
Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2)
```

`true`

