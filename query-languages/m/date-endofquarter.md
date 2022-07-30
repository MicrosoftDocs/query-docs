---
description: "Learn more about: Date.EndOfQuarter"
title: "Date.EndOfQuarter | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Date.EndOfQuarter

## Syntax

<pre>
Date.EndOfQuarter(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns a `date`, `datetime`, or `datetimezone` value representing the end of the quarter in `dateTime`. Time zone information is preserved.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the end of the quarter is calculated.

## Example 1

Find the end of the quarter for October 10th, 2011, 8:00AM (`#datetime(2011, 10, 10, 8, 0, 0)`).

**Usage**

```powerquery-m
Date.EndOfQuarter(#datetime(2011, 10, 10, 8, 0, 0))
```

**Output**

`#datetime(2011, 12, 31, 23, 59, 59.9999999)`
