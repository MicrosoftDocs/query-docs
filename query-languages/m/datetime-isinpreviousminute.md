---
title: "DateTime.IsInPreviousMinute | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.IsInPreviousMinute

## Syntax

<pre>
DateTime.IsInPreviousMinute(<b>dateTime</b> as any) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the previous minute, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the minute before the current system time is in the previous minute.

```powerquery-m
DateTime.IsInPreviousMinute(DateTime.FixedLocalNow() - #duration(0, 0, 1, 0))
```

`true`
