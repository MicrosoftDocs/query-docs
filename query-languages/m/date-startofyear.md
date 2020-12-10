---
title: "Date.StartOfYear | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.StartOfYear

## Syntax

<pre>
Date.StartOfYear(<b>dateTime</b> as any) as any
</pre>
  
## About  
Returns the first value of the year given a `date`, `datetime`, or `datetimezone` value.

## Example 1
Find the start of the year for October 10th, 2011, 8:10:32AM (`#datetime(2011, 10, 10, 8, 10, 32)`).

```powerquery-m
Date.StartOfYear(#datetime(2011, 10, 10, 8, 10, 32))
```

`#datetime(2011, 1, 1, 0, 0, 0)`
