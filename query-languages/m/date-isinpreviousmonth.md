---
title: "Date.IsInPreviousMonth | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInPreviousMonth

  
## About

Indicates whether the given datetime value <code>dateTime</code> occurs during the previous month, as determined by the current date and time on the system. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>
  
## Syntax

<pre>  
Date.IsInPreviousMonth(<b>dateTime</b> as any) as nullable logical
</pre>
  
## Example 1

Determine if the month before the current system time is in the previous month.

```powerquery-m
Date.IsInPreviousMonth(Date.AddMonths(DateTime.FixedLocalNow(), -1))
`

`true`
  
