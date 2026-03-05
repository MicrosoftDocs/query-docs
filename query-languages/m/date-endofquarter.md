---
description: "Learn more about: Date.EndOfQuarter"
title: "Date.EndOfQuarter"
ms.subservice: m-source
ms.topic: reference
---
# Date.EndOfQuarter

## Syntax

<pre>
Date.EndOfQuarter(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the end of the quarter that contains `dateTime`. Time zone information is preserved.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the end of the quarter is calculated.

## Example 1

Find the end of the quarter for October 10th, 2011, 8:00AM.

**Usage**

```powerquery-m
Date.EndOfQuarter(#datetime(2011, 10, 10, 8, 0, 0))
```

**Output**

`#datetime(2011, 12, 31, 23, 59, 59.9999999)`
