---
title: "Date.IsInNextMonth | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInNextMonth

## Syntax

<pre>
Date.IsInNextMonth(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` occurs during the next month, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the month after the current system time is in the next month.

```powerquery-m
Date.IsInNextMonth(Date.AddMonths(DateTime.FixedLocalNow(), 1))
```

`true`
