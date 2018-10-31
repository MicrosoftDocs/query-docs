---
title: "Date.IsInNextNYears | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNYears
`Date.IsInNextNYears(**dateTime** as any, **years** as number) as nullable logical`

## About
Indicates whether the given datetime value `dateTime` occurs during the next number of years, as determined by the current date and time on the system. 
* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `years`: The number of years.

## Example 
Determine if the year after the current system time is in the next two years.

`Date.IsInNextNYears(Date.AddYears(DateTime.FixedLocalNow(), 1), 2)`

`true`

