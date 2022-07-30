---
description: "Learn more about: Duration.Minutes"
title: "Duration.Minutes"
ms.date: 7/18/2022
ms.service: powerquery
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

Returns the minutes portion of `duration`.

## Example 1

Extract the minutes from a duration value.

**Usage**

```powerquery-m
Duration.Minutes(#duration(5, 4, 3, 2))
```

**Output**

`3`
