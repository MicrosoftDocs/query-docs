---
title: "Date.IsInNextMonth | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextMonth
  
## About  

Indicates whether the given datetime value <code>dateTime</code> occurs during the next month, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current month. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Syntax

<pre>
Date.IsInNextMonth(<b>dateTime</b> as any) as nullable logical
</pre>

## Example 1

Determine if the month after the current system time is in the next month.

`Date.IsInNextMonth(Date.AddMonths(DateTime.FixedLocalNow(), 1))`

`true`
  
