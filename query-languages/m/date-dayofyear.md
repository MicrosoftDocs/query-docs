---
description: "Learn more about: Date.DayOfYear"
title: "Date.DayOfYear | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

**Usage**

```powerquery-m
Date.DayOfYear(#date(2011, 03, 01))
```

**Output**

`60`
