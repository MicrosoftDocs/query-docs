---
title: "Date.IsInNextNYears | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNYears

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of years, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `years`: The number of years.

## Syntax

<pre>
Date.IsInNextNYears(**dateTime** as any, **years** as number) as nullable logical
</pre>

## Example 

Determine if the year after the current system time is in the next two years.

```powerquery-m
Date.IsInNextNYears(Date.AddYears(DateTime.FixedLocalNow(), 1), 2)
```

`true`

