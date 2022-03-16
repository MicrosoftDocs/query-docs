---
description: "Learn more about: Date.IsInCurrentQuarter"
title: "Date.IsInCurrentQuarter | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInCurrentQuarter

## Syntax

<pre>
Date.IsInCurrentQuarter(<b>dateTime</b> as any) as nullable logical 
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the current quarter, as determined by the current date and time on the system.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current quarter.

**Usage**

```powerquery-m
Date.IsInCurrentQuarter(DateTime.FixedLocalNow())
```

**Output**

`true`
