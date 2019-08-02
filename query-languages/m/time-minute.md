---
title: "Time.Minute | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Time.Minute

## Syntax

<pre> 
Time.Minute(<b>dateTime</b> as any) as nullable number
</pre>
  
## About  
Returns the minute component of the provided `time`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1
Find the minute in #datetime(2011, 12, 31, 9, 15, 36).

```powerquery-m
Time.Minute(#datetime(2011, 12, 31, 9, 15, 36))
```

`15`
