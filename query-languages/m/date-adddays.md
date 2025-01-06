---
description: "Learn more about: Date.AddDays"
title: "Date.AddDays"
ms.subservice: m-source
---
# Date.AddDays

## Syntax

<pre>
Date.AddDays(<b>dateTime</b> as any, <b>numberOfDays</b> as number) as any
</pre>

## About

Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfDays` days to the `datetime` value `dateTime`.

* `dateTime`: The `date`, `datetime`, or `datetimezone` value to which days are being added.
* `numberOfDays`: The number of days to add.

## Example 1

Add 5 days to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

**Usage**

```powerquery-m
Date.AddDays(#date(2011, 5, 14), 5)
```

**Output**

`#date(2011, 5, 19)`
