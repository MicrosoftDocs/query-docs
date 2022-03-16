---
description: "Learn more about: Date.IsInYearToDate"
title: "Date.IsInYearToDate | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInYearToDate

## Syntax

<pre>
Date.IsInYearToDate(<b>dateTime</b> as any) as nullable logical  
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the current year and is on or before the current day, as determined by the current date and time on the system.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the year to date.

**Usage**

```powerquery-m
Date.IsInYearToDate(DateTime.FixedLocalNow())
```

**Output**

`true`
