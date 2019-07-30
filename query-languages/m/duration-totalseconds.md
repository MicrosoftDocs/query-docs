---
title: "Duration.TotalSeconds | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.TotalSeconds

## Syntax

<pre>
Duration.TotalSeconds(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About  
Returns the total seconds spanned by the provided `duration` value, `duration`.

## Example 1
Find the total seconds spanned in #duration(5, 4, 3, 2).

```powerquery-m
Duration.TotalSeconds(#duration(5, 4, 3, 2))
```

`446582`
