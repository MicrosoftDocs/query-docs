---
description: "Learn more about: Duration.TotalDays"
title: "Duration.TotalDays | Microsoft Docs"
ms.date: 7/18/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Duration.TotalDays

## Syntax

<pre>
Duration.TotalDays(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About

Returns the total days spanned by `duration`.

## Example 1

Find the total days spanned by a duration value.

**Usage**

```powerquery-m
Duration.TotalDays(#duration(5, 4, 3, 2))
```

**Output**

`5.1687731481481478`
