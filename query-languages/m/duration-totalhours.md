---
description: "Learn more about: Duration.TotalHours"
title: "Duration.TotalHours"
ms.date: 7/18/2022
ms.service: powerquery
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

Returns the total hours spanned by `duration`.

## Example 1

Find the total hours spanned by a duration value.

**Usage**

```powerquery-m
Duration.TotalHours(#duration(5, 4, 3, 2))
```

**Output**

`124.05055555555555`
