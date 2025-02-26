---
description: "Learn more about: Date.DaysInMonth"
title: "Date.DaysInMonth"
ms.subservice: m-source
---
# Date.DaysInMonth

## Syntax

<pre>
Date.DaysInMonth(<b>dateTime</b> as any) as nullable number
</pre>
  
## About

Returns the number of days in the month in the `date`, `datetime`, or `datetimezone` value `dateTime`.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value for which the number of days in the month is returned.

## Example 1

Number of days in the month December as represented by `#date(2011, 12, 01)`.

**Usage**

```powerquery-m
Date.DaysInMonth(#date(2011, 12, 01))
```

**Output**

`31`
