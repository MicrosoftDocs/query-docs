---
title: "Date.IsInNextNQuarters | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNQuarters

## Syntax

<pre>
Date.IsInNextNQuarters(**dateTime** as any, **quarters** as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of quarters, as determined by the current date and time on the system. 
- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
- `quarters`: The number of quarters.

## Example 
Determine if the quarter after the current system time is in the next two quarters.

```powerquery-m
Date.IsInNextNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), 1), 2)
```

`true`

