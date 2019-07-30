---
title: "Date.DayOfYear | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.DayOfYear

## Syntax

<pre>
Date.DayOfYear(<b>dateTime</b> as any) as nullable number
</pre>
  
## About  
Returns a number representing the day of the year in the provided `date`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1
The number of the day March 1st, 2011 (`#date(2011, 03, 01)`).

```powerquery-m
Date.DayOfYear(#date(2011, 03, 01))
```

`60`