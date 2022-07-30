---
description: "Learn more about: Date.IsInNextNYears"
title: "Date.IsInNextNYears"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInNextNYears

## Syntax

<pre>
Date.IsInNextNYears(<b>dateTime</b> as any, <b>years</b> as number) as nullable logical
</pre>

## About

Indicates whether the given datetime value `dateTime` occurs during the next number of years, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.
 * `years`: The number of years.

## Example 1

Determine if the year after the current system time is in the next two years.

**Usage**

```powerquery-m
Date.IsInNextNYears(Date.AddYears(DateTime.FixedLocalNow(), 1), 2)
```

**Output**

`true`
