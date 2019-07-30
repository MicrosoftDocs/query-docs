---
title: "DateTime.IsInPreviousNHours | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousNHours

## Syntax

<pre>
DateTime.IsInPreviousNHours(<b>dateTime</b> as any, <b>hours</b> as number) as nullable logical
</pre>
  
## About 
Indicates whether the given datetime value `dateTime` occurs during the previous number of hours, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current hour. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>hours</code>: The number of hours.</li> </ul>

## Example 1
Determine if the hour before the current system time is in the previous two hours.

```powerquery-m
DateTime.IsInPreviousNHours(DateTime.FixedLocalNow() - #duration(0,2,0,0), 2)
```

`true`
