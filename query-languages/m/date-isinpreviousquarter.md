---
title: "Date.IsInPreviousQuarter | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousQuarter
  
## About

Indicates whether the given datetime value <code>dateTime</code> occurs during the previous quarter, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>  
  
## Syntax

<pre>
Date.IsInPreviousQuarter(<b>dateTime</b> as any) as nullable logical
</pre>
  
## Example 1
Determine if the quarter before the current system time is in the previous quarter.

```powerquery-m
Date.IsInPreviousQuarter(Date.AddQuarters(DateTime.FixedLocalNow(), -1))
```

`true`
  
