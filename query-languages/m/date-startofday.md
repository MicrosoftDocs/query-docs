---
title: "Date.StartOfDay | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.StartOfDay

## Syntax

<pre> 
Date.StartOfDay(<b>dateTime</b> as any) as any
</pre> 
  
## About  
Returns the first value of the day `dateTime`. `dateTime` must be a `date`, `datetime`, or `datetimezone` value.

## Example 1
Find the start of the day for October 10th, 2011, 8:00AM (`#datetime(2011, 10, 10, 8, 0, 0)`).

```powerquery-m
Date.StartOfDay(#datetime(2011, 10, 10, 8, 0, 0))
```

```powerquery-m
#datetime(2011, 10, 10, 0, 0, 0)
```
