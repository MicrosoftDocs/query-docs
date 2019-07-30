---
title: "Date.EndOfQuarter | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.EndOfQuarter

## Syntax

<pre>
Date.EndOfQuarter(<b>dateTime</b> as any) as any 
</pre> 
  
## About  
Returns a `date`, `datetime`, or `datetimezone` value representing the end of the quarter in `dateTime`. Time zone information is preserved. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the end of the quarter is calculated.</li> </ul>

## Example 1
Find the end of the quarter for October 10th, 2011, 8:00AM (`#datetime(2011, 10, 10, 8, 0, 0)`).

```powerquery-m
Date.EndOfQuarter(#datetime(2011, 10, 10, 8, 0, 0))
```

```powerquery-m
#datetime(2011, 12, 31, 23, 59, 59.9999999)
```
