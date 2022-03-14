---
description: "Learn more about: Duration.Days"
title: "Duration.Days | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Duration.Days

## Syntax

<pre>
Duration.Days(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About

Returns the day component of the provided `duration` value, `duration`.

## Example 1

Find the day in #duration(5, 4, 3, 2).

**Usage**

```powerquery-m
Duration.Days(#duration(5, 4, 3, 2))
```

**Output**

`5`
