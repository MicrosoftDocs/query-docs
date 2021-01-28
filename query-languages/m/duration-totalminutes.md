---
description: "Learn more about: Duration.TotalMinutes"
title: "Duration.TotalMinutes | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.TotalMinutes

## Syntax

<pre>
Duration.TotalMinutes(<b>duration</b> as nullable duration) as nullable number 
</pre>
  
## About  
Returns the total minutes spanned by the provided `duration` value, `duration`.

## Example 1
Find the total minutes spanned in #duration(5, 4, 3, 2).

```powerquery-m
Duration.TotalMinutes(#duration(5, 4, 3, 2))
```

`7443.0333333333338`
