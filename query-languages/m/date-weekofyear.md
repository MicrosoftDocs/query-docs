---
title: "Date.WeekOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.WeekOfYear

  <code>Date.WeekOfYear(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number</code>

## About 

Returns a number from 1 to 54 indicating which week of the year the date, <code>dateTime</code>, falls in. <ul> <li><code>dateTime</code>: A <code>datetime</code> value for which the week-of-the-year is determined.</li> </ul>

## Example 1

Determine which week of the year March 23rd, 2011 falls in (<code>#date(2011, 03, 23)</code>).

<code>Date.WeekOfYear(#date(2011, 03, 23))</code>

<code>13</code>
