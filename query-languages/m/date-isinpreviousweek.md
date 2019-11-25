---
title: "Date.IsInPreviousWeek | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.IsInPreviousWeek

## Syntax

<pre>
Date.IsInPreviousWeek(<b>dateTime</b> as any) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the previous week, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current week. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the week before the current system time is in the previous week.

```powerquery-m
Date.IsInPreviousWeek(Date.AddDays(DateTime.FixedLocalNow(), -7))
```

`true`
