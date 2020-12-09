---
title: "Duration.TotalHours | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.TotalHours

## Syntax

<pre>
Duration.TotalHours(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About  
Returns the total hours spanned by the provided `duration` value, `duration`.

## Example 1
Find the total hours spanned in #duration(5, 4, 3, 2).

```powerquery-m
Duration.TotalHours(#duration(5, 4, 3, 2))
```

`124.05055555555555`
