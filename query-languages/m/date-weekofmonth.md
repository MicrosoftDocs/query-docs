---
title: "Date.WeekOfMonth | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.WeekOfMonth

## Syntax

<pre>
Date.WeekOfMonth(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number  
</pre>
  
## About  
Returns a number from 1 to 5 indicating which week of the year month the date `dateTime` falls in. <ul> <li><code>dateTime</code>: A <code>datetime</code> value for which the week-of-the-month is determined.</li> </ul>

## Example 1
Determine which week of March the 15th falls on in 2011 (`#date(2011, 03, 15)`).

```powerquery-m
Date.WeekOfMonth(#date(2011, 03, 15))
```

`3`
