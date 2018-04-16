---
title: "Date.IsInCurrentDay | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInCurrentDay
<code>Date.IsInCurrentDay(**dateTime** as any) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the current day, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.

## Example 
Determine if the current system time is in the current day.

<code>Date.IsInCurrentDay(DateTime.FixedLocalNow())</code>

<code>true</code>

