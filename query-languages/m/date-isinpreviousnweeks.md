---
title: "Date.IsInPreviousNWeeks | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNWeeks
<code>Date.IsInPreviousNWeeks(**dateTime** as any, **weeks** as number) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of weeks, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.
* <code>weeks</code>: The number of weeks.

## Example 
Determine if the week before the current system time is in the previous two weeks.

<code>Date.IsInPreviousNWeeks(Date.AddDays(DateTime.FixedLocalNow(), -7), 2)</code>

<code>true</code>

