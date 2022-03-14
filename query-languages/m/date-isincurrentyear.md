---
description: "Learn more about: Date.IsInCurrentYear"
title: "Date.IsInCurrentYear | Microsoft Docs"
ms.date: 3/112022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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
