---
description: "Learn more about: Duration.Minutes"
title: "Duration.Minutes | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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
