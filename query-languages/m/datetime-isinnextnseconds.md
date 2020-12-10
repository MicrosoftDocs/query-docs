---
title: "DateTime.IsInNextNSeconds | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.IsInNextNSeconds

## Syntax

<pre>
DateTime.IsInNextNSeconds(<b>dateTime</b> as any, <b>seconds</b> as number) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the next number of seconds, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>seconds</code>: The number of seconds.</li> </ul>

## Example 1
Determine if the second after the current system time is in the next two seconds.

```powerquery-m
DateTime.IsInNextNSeconds(DateTime.FixedLocalNow() + #duration(0, 0, 0, 2), 2)
```

`true`

