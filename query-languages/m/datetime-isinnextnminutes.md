---
title: "DateTime.IsInNextNMinutes | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextNMinutes

## Syntax

<pre>
DateTime.IsInNextNMinutes(<b>dateTime</b> as any, <b>minutes</b> as number) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the next number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>minutes</code>: The number of minutes.</li> </ul>

## Example 1
Determine if the minute after the current system time is in the next two minutes.

```powerquery-m
DateTime.IsInNextNMinutes(DateTime.FixedLocalNow() + #duration(0,0,2,0), 2)
```

`true`

