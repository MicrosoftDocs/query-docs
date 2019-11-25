---
title: "DateTime.IsInPreviousNMinutes | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# DateTime.IsInPreviousNMinutes

## Syntax

<pre>
DateTime.IsInPreviousNMinutes(<b>dateTime</b> as any, <b>minutes</b> as number) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the previous number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>minutes</code>: The number of minutes.</li> </ul>

## Example 1
Determine if the minute before the current system time is in the previous two minutes.

```powerquery-m
DateTime.IsInPreviousNMinutes(DateTime.FixedLocalNow() - #duration(0,0,2,0), 2)
```

`true`
