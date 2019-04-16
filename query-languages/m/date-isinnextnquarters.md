---
title: "Date.IsInNextNQuarters | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNQuarters

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter.

- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
- `quarters`: The number of quarters.

## Syntax

<pre>
Date.IsInNextNQuarters(**dateTime** as any, **quarters** as number) as nullable logical
</pre>

## Example 

Determine if the quarter after the current system time is in the next two quarters.

```powerquery-m
Date.IsInNextNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), 1), 2)
```

`true`

