---
description: "Learn more about: Date.AddWeeks"
title: "Date.AddWeeks"
ms.subservice: m-source
---
# Date.AddWeeks

## Syntax

<pre>
Date.AddWeeks(<b>dateTime</b> as any, <b>numberOfWeeks</b> as number) as any
</pre>

## About

Returns the `date`, `datetime`, or `datetimezone` result from adding `numberOfWeeks` weeks to the `datetime` value `dateTime`.

* `dateTime`: The `date`, `datetime`, or `datetimezone` value to which weeks are being added.
* `numberOfWeeks`: The number of weeks to add.

## Example 1

Add 2 weeks to the `date`, `datetime`, or `datetimezone` value representing the date 5/14/2011.

**Usage**

```powerquery-m
Date.AddWeeks(#date(2011, 5, 14), 2)
```

**Output**

`#date(2011, 5, 28)`
