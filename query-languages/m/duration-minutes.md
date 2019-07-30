---
title: "Duration.Minutes | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.Minutes

## Syntax

<pre>
Duration.Minutes(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About  
Returns the minutes component of the provided `duration` value, `duration`.

## Example 1
Find the minutes in #duration(5, 4, 3, 2).

```powerquery-m
Duration.Minutes(#duration(5, 4, 3, 2))
```

`3`
