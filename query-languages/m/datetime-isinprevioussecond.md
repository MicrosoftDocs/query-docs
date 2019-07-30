---
title: "DateTime.IsInPreviousSecond | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousSecond

## Syntax

<pre>
DateTime.IsInPreviousSecond(<b>dateTime</b> as any) as nullable logical
</pre>

## About  
Indicates whether the given datetime value `dateTime` occurs during the previous second, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the second before the current system time is in the previous second.

```powerquery-m
DateTime.IsInPreviousSecond(DateTime.FixedLocalNow() - #duration(0,0,0,1))
```

`true`
