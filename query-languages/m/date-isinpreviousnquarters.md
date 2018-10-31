---
title: "Date.IsInPreviousNQuarters | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNQuarters
`Date.IsInPreviousNQuarters(**dateTime** as any, **quarters** as number) as nullable logical`
## About
Indicates whether the given datetime value `dateTime` occurs during the previous number of quarters, as determined by the current date and time on the system. 
* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated. 
* `quarters`: The number of quarters.

## Example 1
Determine if the quarter before the current system time is in the previous two quarters.

`Date.IsInPreviousNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), -1), 2)`

`true`

