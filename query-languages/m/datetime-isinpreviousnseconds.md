---
description: "Learn more about: DateTime.IsInPreviousNSeconds"
title: "DateTime.IsInPreviousNSeconds | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.IsInPreviousNSeconds

## Syntax

<pre>
DateTime.IsInPreviousNSeconds(<b>dateTime</b> as any, <b>seconds</b> as number) as nullable logical
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` occurs during the previous number of seconds, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>seconds</code>: The number of seconds.</li> </ul>

## Example 1
Determine if the second before the current system time is in the previous two seconds.

```powerquery-m
DateTime.IsInPreviousNSeconds(DateTime.FixedLocalNow() - #duration(0, 0, 0, 2), 2)
```

`true`

