---
description: "Learn more about: Date.IsInNextYear"
title: "Date.IsInNextYear"
ms.date: 3/11/2022
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInNextYear

## Syntax

<pre>
Date.IsInNextYear(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About  

Indicates whether the given datetime value `dateTime` occurs during the next year, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current year.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the year after the current system time is in the next year.

**Usage**

```powerquery-m
Date.IsInNextYear(Date.AddYears(DateTime.FixedLocalNow(), 1))
```

**Output**

`true`
