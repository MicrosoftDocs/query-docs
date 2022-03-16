---
description: "Learn more about: Date.IsInNextNQuarters"
title: "Date.IsInNextNQuarters | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInNextNQuarters

## Syntax

<pre>
Date.IsInNextNQuarters(<b>dateTime</b> as any, <b>quarters</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of quarters, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `quarters`: The number of quarters.

## Example 1

Determine if the quarter after the current system time is in the next two quarters.

**Usage**

```powerquery-m
Date.IsInNextNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), 1), 2)
```

**Output**

`true`
