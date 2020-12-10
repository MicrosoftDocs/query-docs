---
title: "Date.IsInNextQuarter | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.IsInNextQuarter

## Syntax

<pre>
Date.IsInNextQuarter(<b>dateTime</b> as any) as nullable logical
</pre>  

## About  
Indicates whether the given datetime value `dateTime` occurs during the next quarter, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

####Example 1
Determine if the quarter after the current system time is in the next quarter.

```powerquery-m
Date.IsInNextQuarter(Date.AddQuarters(DateTime.FixedLocalNow(), 1))
```

`true`
