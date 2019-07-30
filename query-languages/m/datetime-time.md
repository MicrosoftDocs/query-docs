---
title: "DateTime.Time | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.Time

## Syntax

<pre>
DateTime.Time(<b>dateTime</b> as any) as nullable time 
</pre>
  
## About  
Returns the time part of the given datetime value, `dateTime`.

## Example 1
Find the time value of #datetime(2010, 12, 31, 11, 56, 02).

```powerquery-m
DateTime.Time(#datetime(2010, 12, 31, 11, 56, 02))
```

`#time(11, 56, 2)`
