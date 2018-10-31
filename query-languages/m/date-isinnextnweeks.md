---
title: "Date.IsInNextNWeeks | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNWeeks

## Syntax

<pre>
Date.IsInNextNWeeks(**dateTime** as any, **weeks** as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of weeks, as determined by the current date and time on the system. 
- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
- `weeks`: The number of weeks.

## Example 
Determine if the week after the current system time is in the next two weeks.

```powerquery-m
Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2)
```

`true`

