---
title: "Date.StartOfWeek | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.StartOfWeek

## Syntax

<pre>
Date.StartOfWeek(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as any 
</pre>
  
## About  
Returns the first value of the week given a `date`, `datetime`, or `datetimezone` value.

## Example 1
Find the start of the week for October 10th, 2011, 8:10:32AM (`#datetime(2011, 10, 10, 8, 10, 32)`).

```powerquery-m
Date.StartOfWeek(#datetime(2011, 10, 10, 8, 10, 32))
```

`#datetime(2011, 10, 9, 0, 0, 0)`
