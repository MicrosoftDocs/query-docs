---
title: "Date.AddDays | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.AddDays

## Syntax

<pre>
Date.AddDays(<b>dateTime</b> as any, <b>numberOfDays</b> as number) as any  
</pre> 
  
## About  
Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfDays` days to the `datetime` value `dateTime`. <ul> <li><code>dateTime</code>: The <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to which days are being added.</li> <li><code>numberOfDays</code>: The number of days to add.</li> </ul>

## Example 1
Add 5 days to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

```powerquery-m
Date.AddDays(#date(2011, 5, 14), 5)
```

```powerquery-m
#date(2011, 5, 19)
```