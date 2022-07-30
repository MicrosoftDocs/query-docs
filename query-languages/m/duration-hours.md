---
description: "Learn more about: Duration.Hours"
title: "Duration.Hours"
ms.date: 7/18/2022
ms.service: powerquery

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

Returns the hours portion of `duration`.

## Example 1

Extract the hours from a duration value.

**Usage**

```powerquery-m
Duration.Hours(#duration(5, 4, 3, 2))
```

**Output**

`4`
