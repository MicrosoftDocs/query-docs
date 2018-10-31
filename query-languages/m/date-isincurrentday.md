---
title: "Date.IsInCurrentDay | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInCurrentDay
`Date.IsInCurrentDay(**dateTime** as any) as nullable logical`

## About
Indicates whether the given datetime value `dateTime` occurs during the current day, as determined by the current date and time on the system. 
- `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 
Determine if the current system time is in the current day.

`Date.IsInCurrentDay(DateTime.FixedLocalNow())`

`true`

