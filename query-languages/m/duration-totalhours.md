---
description: "Learn more about: Duration.TotalHours"
title: "Duration.TotalHours | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Duration.TotalHours(#duration(5, 4, 3, 2))
```

**Output**

`124.05055555555555`
