---
description: "Learn more about: Duration.ToRecord"
title: "Duration.ToRecord | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Duration.ToRecord

## Syntax

<pre>
Duration.ToRecord(<b>duration</b> as duration) as record
</pre>
  
## About

Returns a record containing the parts the duration value, `duration`.

* `duration`: A `duration` from which the record is created.

## Example 1

Convert `#duration(2, 5, 55, 20)` into a record of its parts including days, hours, minutes, and seconds if applicable.

**Usage**

```powerquery-m
Duration.ToRecord(#duration(2, 5, 55, 20))
```

**Output**

```powerquery-m
[
    Days = 2,
    Hours = 5,
    Minutes = 55,
    Seconds = 20
]
```
