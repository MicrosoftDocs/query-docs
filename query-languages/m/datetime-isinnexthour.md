---
title: "DateTime.IsInNextHour | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextHour

## About  

Indicates whether the given datetime value <code>dateTime</code> occurs during the next hour, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Syntax

<pre>
DateTime.IsInNextHour(<b>dateTime</b> as any) as nullable logical 
</pre>

## Example 1  

Determine if the hour after the current system time is in the next hour.

```powerquery-m
DateTime.IsInNextHour(DateTime.FixedLocalNow() + #duration(0,1,0,0))
```

`true`
