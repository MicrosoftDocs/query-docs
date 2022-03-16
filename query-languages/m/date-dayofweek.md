---
description: "Learn more about: Date.DayOfWeek"
title: "Date.DayOfWeek | Microsoft Docs"
ms.date: 3/11/2022
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

Returns a number (from 0 to 6) indicating the day of the week of the provided `dateTime`.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value.
* `firstDayOfWeek`: A `Day` value indicating which day should be considered the first day of the week. Allowed values are [Day.Sunday](/powerquery-m/day-sunday), [Day.Monday](/powerquery-m/day-monday), [Day.Tuesday](/powerquery-m/day-tuesday), [Day.Wednesday](/powerquery-m/day-wednesday), [Day.Thursday](/powerquery-m/day-Thursday), [Day.Friday](/powerquery-m/day-friday), or [Day.Saturday](/powerquery-m/day-saturday). If unspecified, a culture-dependent default is used.

## Example 1

Get the day of the week represented by Monday, February 21st, 2011, treating Sunday as the first day of the week.

**Usage**

```powerquery-m
Date.DayOfWeek(#date(2011, 02, 21), Day.Sunday)`
```

**Output**

`1`

## Example 2

Get the day of the week represented by Monday, February 21st, 2011, treating Monday as the first day of the week.

**Usage**

```powerquery-m
Date.DayOfWeek(#date(2011, 02, 21), Day.Monday)
```

**Output**

`0`
