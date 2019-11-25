---
title: "Date.IsInCurrentMonth | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Date.IsInCurrentMonth

## Syntax

<pre>
Date.IsInCurrentMonth(<b>dateTime</b> as any) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` occurs during the current month, as determined by the current date and time on the system. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the current system time is in the current month.

```powerquery-m
Date.IsInCurrentMonth(DateTime.FixedLocalNow())
```

`true`
