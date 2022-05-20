---
description: "Learn more about: Date.IsInPreviousQuarter"
title: "Date.IsInPreviousQuarter | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.IsInPreviousQuarter

## Syntax

<pre>
Date.IsInPreviousQuarter(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the previous quarter, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the quarter before the current system time is in the previous quarter.

**Usage**

```powerquery-m
Date.IsInPreviousQuarter(Date.AddQuarters(DateTime.FixedLocalNow(), -1))
```

**Output**

`true`
