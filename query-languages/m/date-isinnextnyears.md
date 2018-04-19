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
<code>Date.IsInNextNYears(**dateTime** as any, **years** as number) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the next number of years, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.
* <code>years</code>: The number of years.

## Example 
Determine if the year after the current system time is in the next two years.

<code>Date.IsInNextNYears(Date.AddYears(DateTime.FixedLocalNow(), 1), 2)</code>

<code>true</code>

