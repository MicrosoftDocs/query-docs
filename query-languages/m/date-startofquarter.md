---
description: "Learn more about: Date.StartOfQuarter"
title: "Date.StartOfQuarter"
ms.date: 3/11/2022
---
# Date.StartOfQuarter

## Syntax

<pre>
Date.StartOfQuarter(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the first value of the quarter <`dateTime`. `dateTime` must be a `date`, `datetime`, or `datetimezone` value.

## Example 1

Find the start of the quarter for October 10th, 2011, 8:00AM (`#datetime(2011, 10, 10, 8, 0, 0)`).

**Usage**

```powerquery-m
Date.StartOfQuarter(#datetime(2011, 10, 10, 8, 0, 0))
```

**Output**

`#datetime(2011, 10, 1, 0, 0, 0)`
