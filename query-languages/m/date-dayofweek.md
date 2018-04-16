---
title: "Date.DayOfWeek | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DayOfWeek

<code>Date.DayOfWeek(**dateTime** as any, optional **firstDayOfWeek** as nullable number) as nullable number</code>

## About

Returns a number between 0 and 6 representing the day of the week in the provided datetime value <code>dateTime</code>. This function takes an optional Day value, <code>firstDayOfWeek</code>, to set the first day of the week for this relative calculation. The default value firstDay is Day.Sunday. Valid values are: Day.Sunday, Day.Monday, Day.Tuesday, Day.Wednesday, Day.Thursday, Day.Friday, and Day.Saturday. 

* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the day of the week is determined.
 
* <code>firstDayOfWeek</code>: A <code>Day</code> type representing the first day of the week for this calculation.

## Example 1
Get which the day of the week February 21st, 2011 falls on, with (default) Sunday being the first day of the week.

<code>Date.DayOfWeek(#date(2011, 02, 21))</code>

<code>1</code>

## Example 2
Get which day of the week February 21st, 2011 falls on, with Monday being the first day of the week.

<code>Date.DayOfWeek(#date(2011, 02, 21), Day.Monday)</code>

<code>0</code>