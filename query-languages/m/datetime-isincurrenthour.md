---
title: "DateTime.IsInCurrentHour | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.IsInCurrentHour

## Syntax

<pre>
DateTime.IsInCurrentHour(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` occurs during the current hour, as determined by the current date and time on the system. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the current system time is in the current hour.

```powerquery-m
DateTime.IsInCurrentHour(DateTime.FixedLocalNow())
```

`true`

