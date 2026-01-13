---
description: "Learn more about: Date.StartOfMonth"
title: "Date.StartOfMonth"
ms.subservice: m-source
ms.topic: reference
---
# Date.StartOfMonth

## Syntax

<pre>
Date.StartOfMonth(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the start of the month that contains `dateTime`. `dateTime` must be a `date` or `datetime` value.

## Example 1

Find the start of the month for October 10th, 2011, 8:10:32AM.

**Usage**

```powerquery-m
Date.StartOfMonth(#datetime(2011, 10, 10, 8, 10, 32))
```

**Output**

`#datetime(2011, 10, 1, 0, 0, 0)`
