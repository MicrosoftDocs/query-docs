---
title: "Date.IsInNextDay | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextDay
<code>Date.IsInNextDay(**dateTime** as any) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the next day, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.

## Example 
Determine if the day after the current system time is in the next day.

<code>Date.IsInNextDay(Date.AddDays(DateTime.FixedLocalNow(), 1))</code>

<code>true</code>

