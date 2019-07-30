---
title: "Date.StartOfMonth | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.StartOfMonth

## Syntax

<pre>
Date.StartOfMonth(<b>dateTime</b> as any) as any
</pre>
  
## About  
Returns the first value of the month given a `date` or `datetime` type.

## Example 1
Find the start of the month for October 10th, 2011, 8:10:32AM (`#datetime(2011, 10, 10, 8, 10, 32)`).

```powerquery-m
Date.StartOfMonth(#datetime(2011, 10, 10, 8, 10, 32))
```

```powerquery-m
#datetime(2011, 10, 1, 0, 0, 0)
```
