---
description: "Learn more about: DateTime.IsInNextNHours"
title: "DateTime.IsInNextNHours | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTime.IsInNextNHours

## Syntax

<pre>
DateTime.IsInNextNHours(<b>dateTime</b> as any, <b>hours</b> as number) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the next number of hours, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>hours</code>: The number of hours.</li> </ul>

## Example 1
Determine if the hour after the current system time is in the next two hours.

```powerquery-m
DateTime.IsInNextNHours(DateTime.FixedLocalNow() + #duration(0, 2, 0, 0), 2)
```

`true`

