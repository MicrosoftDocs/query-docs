---
title: "Date.IsInNextNWeeks | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNWeeks
<code>Date.IsInNextNWeeks(**dateTime** as any, **weeks** as number) as nullable logical</code>

## About

Indicates whether the given datetime value <code>dateTime</code> occurs during the next number of weeks, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated. 
- <code>weeks</code>: The number of weeks.

## Example 
Determine if the week after the current system time is in the next two weeks.

<code>Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2)</code>

<code>true</code>

