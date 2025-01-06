---
description: "Learn more about: Date.StartOfDay"
title: "Date.StartOfDay"
ms.subservice: m-source
---
# Date.StartOfDay

## Syntax

<pre> 
Date.StartOfDay(<b>dateTime</b> as any) as any
</pre>

## About

Returns the start of the day represented by `dateTime`. `dateTime` must be a `date`, `datetime`, or `datetimezone` value.

## Example 1

Find the start of the day for October 10th, 2011, 8:00AM.

**Usage**

```powerquery-m
Date.StartOfDay(#datetime(2011, 10, 10, 8, 0, 0))
```

**Output**

`#datetime(2011, 10, 10, 0, 0, 0)`
