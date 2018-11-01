---
title: "Date.DayOfWeek | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DayOfWeek

## Syntax

<pre> 
Date.DayOfWeek(**dateTime** as any, optional **firstDayOfWeek** as nullable number) as nullable number
</pre>

## About

Returns a number between 0 and 6 representing the day of the week in the provided datetime value `dateTime`. This function takes an optional Day value, `firstDayOfWeek`, to set the first day of the week for this relative calculation. The default value firstDay is Day.Sunday. Valid values are: Day.Sunday, Day.Monday, Day.Tuesday, Day.Wednesday, Day.Thursday, Day.Friday, and Day.Saturday. 

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the day of the week is determined.
 
* `firstDayOfWeek`: A `Day` type representing the first day of the week for this calculation.

## Example 1
Get which the day of the week February 21st, 2011 falls on, with (default) Sunday being the first day of the week.

`Date.DayOfWeek(#date(2011, 02, 21))`

`1`

## Example 2
Get which day of the week February 21st, 2011 falls on, with Monday being the first day of the week.

```powerquery-m
Date.DayOfWeek(#date(2011, 02, 21), Day.Monday)
```

`0`