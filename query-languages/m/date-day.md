---
title: "Date.Day | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.Day

## Syntax

<pre>
Date.Day(<b>dateTime</b> as any) as nullable number
</pre>
  
## About  
Returns the day component of a `date`, `datetime`, or `datetimezone` value. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the day component is extracted.</li> </ul>

## Example 1
Get the day component of a `date`, `datetime`, or `datetimezone` value representing the date and time of 5/14/2011 05:00:00 PM.

```powerquery-m
Date.Day(#datetime(2011, 5, 14, 17, 0, 0))
```

`14`