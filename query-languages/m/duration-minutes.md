---
description: "Learn more about: Duration.Minutes"
title: "Duration.Minutes | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Duration.Minutes(#duration(5, 4, 3, 2))
```

**Output**

`3`
