---
title: "Duration.Hours | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.Hours

## Syntax

<pre>
Duration.Hours(<b>duration</b> as nullable duration) as nullable number 
</pre>
  
## About  
Returns the hour component of the provided `duration` value, `duration`.

## Example 1
Find the hours in #duration(5, 4, 3, 2).

```powerquery-m
Duration.Hours(#duration(5, 4, 3, 2))
```

`4`
