---
description: "Learn more about: Duration.Seconds"
title: "Duration.Seconds | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Duration.Seconds

## Syntax

<pre>
Duration.Seconds(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About

Returns the seconds component of the provided `duration` value, `duration`.

## Example 1

Find the seconds in #duration(5, 4, 3, 2).

**Usage**

```powerquery-m
Duration.Seconds(#duration(5, 4, 3, 2))
```

**Output**

`2`
