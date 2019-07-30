---
title: "Date.IsInCurrentWeek | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInCurrentWeek

## Syntax

<pre>
Date.IsInCurrentWeek(<b>dateTime</b> as any) as nullable logical 
</pre>
  
## About  
Indicates whether the given datetime value `dateTime` occurs during the current week, as determined by the current date and time on the system. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Example 1
Determine if the current system time is in the current week.

```powerquery-m
Date.IsInCurrentWeek(DateTime.FixedLocalNow())
```

`true`
