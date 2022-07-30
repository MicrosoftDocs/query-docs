---
description: "Learn more about: Date.WeekOfMonth"
title: "Date.WeekOfMonth"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.WeekOfMonth

## Syntax

<pre>
Date.WeekOfMonth(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as nullable number  
</pre>
  
## About

Returns a number from 1 to 6 indicating which week of the month the date `dateTime` falls in. 

* `dateTime`: A `datetime` value for which the week-of-the-month is determined.

## Example 1

Determine which week of March the 15th falls on in 2011 (`#date(2011, 03, 15)`).

**Usage**

```powerquery-m
Date.WeekOfMonth(#date(2011, 03, 15))
```

**Output**

`3`
