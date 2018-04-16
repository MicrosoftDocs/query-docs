---
title: "Date.IsInNextNDays | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNDays
<code>Date.IsInNextNDays(**dateTime** as any, **days** as number) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the next number of days, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated. 
- <code>days</code>: The number of days.

## Example 
Determine if the day after the current system time is in the next two days.

<code>Date.IsInNextNDays(Date.AddDays(DateTime.FixedLocalNow(), 1), 2)</code>

<code>true</code>

