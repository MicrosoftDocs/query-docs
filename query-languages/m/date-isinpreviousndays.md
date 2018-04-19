---
title: "Date.IsInPreviousNDays | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNDays
<code>Date.IsInPreviousNDays(**dateTime** as any, **days** as number) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of days, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated. 
* <code>days</code>: The number of days.

## Example 1
Determine if the day before the current system time is in the previous two days.

<code>Date.IsInPreviousNDays(Date.AddDays(DateTime.FixedLocalNow(), -1), 2)</code>

<code>true</code>

