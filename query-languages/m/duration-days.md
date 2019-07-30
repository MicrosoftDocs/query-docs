---
title: "Duration.Days | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.Days

## Syntax

<pre>
Duration.Days(<b>duration</b> as nullable duration) as nullable number
</pre> 
  
## About  
Returns the day component of the provided `duration` value, `duration`.

## Example 1
Find the day in #duration(5, 4, 3, 2).

```powerquery-m
Duration.Days(#duration(5, 4, 3, 2))
```

`5`
