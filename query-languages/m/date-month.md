---
description: "Learn more about: Date.Month"
title: "Date.Month"
ms.subservice: m-source
ms.topic: reference
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
