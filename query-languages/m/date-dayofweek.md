---
description: "Learn more about: Date.DayOfWeek"
title: "Date.DayOfWeek | Microsoft Docs"
ms.date: 6/13/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.DayOfWeek

## Syntax

<pre> 
Date.DayOfWeek(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number
</pre>

## About

Returns a number (from 0 to 6) indicating the day of the week of the provided <code>dateTime</code>. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value.</li> <li><code>firstDayOfWeek</code>: A <code>Day</code> value indicating which day should be considered the first day of the week. Allowed values are Day.Sunday, Day.Monday, Day.Tuesday, Day.Wednesday, Day.Thursday, Day.Friday, or Day.Saturday. If unspecified, a culture-dependent default is used.</li> </ul>

## Example 1
Get the day of the week represented by Monday, February 21st, 2011, treating Sunday as the first day of the week.

```powerquery-m
Date.DayOfWeek(#date(2011, 02, 21), Day.Sunday)`
```   

`1`

## Example 2
Get the day of the week represented by Monday, February 21st, 2011, treating Monday as the first day of the week.

```powerquery-m
Date.DayOfWeek(#date(2011, 02, 21), Day.Monday)
```

`0`
