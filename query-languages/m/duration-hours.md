---
description: "Learn more about: Duration.Hours"
title: "Duration.Hours | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Duration.Hours(#duration(5, 4, 3, 2))
```

**Output**

`4`
