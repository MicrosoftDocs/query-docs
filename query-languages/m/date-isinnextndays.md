---
title: "Date.IsInNextNDays | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNDays
`Date.IsInNextNDays(**dateTime** as any, **days** as number) as nullable logical`

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of days, as determined by the current date and time on the system. 
- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
- `days`: The number of days.

## Example 
Determine if the day after the current system time is in the next two days.

`Date.IsInNextNDays(Date.AddDays(DateTime.FixedLocalNow(), 1), 2)`

`true`

