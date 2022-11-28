---
description: "Learn more about: Date.StartOfYear"
title: "Date.StartOfYear"
ms.date: 11/14/2022
---
# Date.StartOfYear

## Syntax

<pre>
Date.StartOfYear(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the start of the year that contains `dateTime`. `dateTime` must be a `date`, `datetime`, or `datetimezone` value.

## Example 1

Find the start of the year for October 10th, 2011, 8:10:32AM.

**Usage**

```powerquery-m
Date.StartOfYear(#datetime(2011, 10, 10, 8, 10, 32))
```

**Output**

`#datetime(2011, 1, 1, 0, 0, 0)`
