---
description: "Learn more about: Date.Month"
title: "Date.Month"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.Month

## Syntax

<pre>
Date.Month(<b>dateTime</b> as any) as nullable number
</pre>
  
## About

Returns the month component of the provided `datetime` value, `dateTime`.

## Example 1

Find the month in #datetime(2011, 12, 31, 9, 15, 36).

**Usage**

```powerquery-m
Date.Month(#datetime(2011, 12, 31, 9, 15, 36))
```

**Output**

`12`
