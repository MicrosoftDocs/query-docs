---
description: "Learn more about: Date.IsInCurrentMonth"
title: "Date.IsInCurrentMonth | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInCurrentMonth

## Syntax

<pre>
Date.IsInCurrentMonth(<b>dateTime</b> as any) as nullable logical  
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the current month, as determined by the current date and time on the system.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current month.

**Usage**

```powerquery-m
Date.IsInCurrentMonth(DateTime.FixedLocalNow())
```

**Output**

`true`
