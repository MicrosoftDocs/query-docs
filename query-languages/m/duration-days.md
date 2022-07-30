---
description: "Learn more about: Duration.Days"
title: "Duration.Days"
ms.date: 7/18/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Duration.Days

## Syntax

<pre>
Duration.Days(<b>duration</b> as nullable duration) as nullable number
</pre>
  
## About

Returns the days portion of `duration`.

## Example 1

Extract the days from a duration value.

**Usage**

```powerquery-m
Duration.Days(#duration(5, 4, 3, 2))
```

**Output**

`5`
