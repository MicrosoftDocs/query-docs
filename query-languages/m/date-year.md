---
description: "Learn more about: Date.Year"
title: "Date.Year"
ms.subservice: m-source
ms.topic: reference
---
# Date.Year

<pre>
Date.Year(<b>dateTime</b> as any) as nullable number
</pre>
  
## About

Returns the year component of the provided `datetime` value, `dateTime`.

## Example 1

Find the year in #datetime(2011, 12, 31, 9, 15, 36).

**Usage**

```powerquery-m
Date.Year(#datetime(2011, 12, 31, 9, 15, 36))
```

**Output**

`2011`
