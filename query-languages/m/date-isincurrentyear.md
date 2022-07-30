---
description: "Learn more about: Date.IsInCurrentYear"
title: "Date.IsInCurrentYear"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInCurrentYear

## Syntax

<pre>
Date.IsInCurrentYear(<b>dateTime</b> as any) as nullable logical  
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the current year, as determined by the current date and time on the system.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current year.

**Usage**

```powerquery-m
Date.IsInCurrentYear(DateTime.FixedLocalNow())
```

**Output**

`true`
