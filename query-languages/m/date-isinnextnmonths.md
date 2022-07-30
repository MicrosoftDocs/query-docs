---
description: "Learn more about: Date.IsInNextNMonths"
title: "Date.IsInNextNMonths | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInNextNMonths

<pre>
Date.IsInNextNMonths(<b>dateTime</b> as any, <b>months</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of months, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
* `months`: The number of months.

## Example 1

Determine if the month after the current system time is in the next two months.

**Usage**

```powerquery-m
Date.IsInNextNMonths(Date.AddMonths(DateTime.FixedLocalNow(), 1), 2)
```

**Output**

`true`
