---
title: "Date.IsInPreviousNYears | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousNYears

## Syntax

<pre>
Date.IsInPreviousNYears(**dateTime** as any, **years** as number) as nullable logical
</pre>

## About
Indicates whether the given datetime value `dateTime` occurs during the previous number of years, as determined by the current date and time on the system. 
* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `years`: The number of years.

## Example 
Determine if the year before the current system time is in the previous two years.

```powerquery-m
Date.IsInPreviousNYears(Date.AddYears(DateTime.FixedLocalNow(), -1), 2)
```

`true`

