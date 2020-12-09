---
title: "Date.WeekOfYear | Microsoft Docs"
ms.date: 11/13/2018
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.WeekOfYear

## Syntax

<pre>
Date.WeekOfYear(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number
</pre>

## About 

Returns a number from 1 to 54 indicating which week of the year the date, `dateTime`, falls in. 

- `dateTime`: A `datetime` value for which the week-of-the-year is determined. 

- `firstDayOfWeek`: An optional `Day.Type` value that indicates which day is considered the start of a new week (for example, `Day.Sunday`. If unspecified, a culture-dependent default is used. 


## Example 1

Determine which week of the year March 27th, 2011 falls in (`#date(2011, 03, 27)`).

```powerquery-m
Date.WeekOfYear(#date(2011, 03, 27))
```

`14`

## Example 2

Determine which week of the year March 27th, 2011 falls in (`#date(2011, 03, 27)`), using Monday as the start of a new week.

```powerquery-m
Date.WeekOfYear(#date(2011, 03, 27), Day.Monday)
```

`13`
