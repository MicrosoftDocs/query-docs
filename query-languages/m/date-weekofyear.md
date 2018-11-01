---
title: "Date.WeekOfYear | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.WeekOfYear

## Syntax

<pre>
Date.WeekOfYear(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number
</pre>

## About 

Returns a number from 1 to 54 indicating which week of the year the date, `dateTime`, falls in. <ul> <li>`dateTime`: A `datetime` value for which the week-of-the-year is determined.</li> </ul>

## Example 1

Determine which week of the year March 23rd, 2011 falls in (`#date(2011, 03, 23)`).

```powerquery-m
Date.WeekOfYear(#date(2011, 03, 23))
```

`13`
