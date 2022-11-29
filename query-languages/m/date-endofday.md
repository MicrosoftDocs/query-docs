---
description: "Learn more about: Date.EndOfDay"
title: "Date.EndOfDay"
ms.date: 11/14/2022
---
# Date.EndOfDay

<pre>
Date.EndOfDay(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the end of the day represented by `dateTime`. Time zone information is preserved.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from from which the end of the day is calculated.

## Example 1

Get the end of the day for 5/14/2011 05:00:00 PM.

**Usage**

```powerquery-m
Date.EndOfDay(#datetime(2011, 5, 14, 17, 0, 0))
```

**Output**

`#datetime(2011, 5, 14, 23, 59, 59.9999999)`

## Example 2

Get the end of the day for 5/17/2011 05:00:00 PM -7:00.

**Usage**

```powerquery-m
Date.EndOfDay(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

**Output**

`#datetimezone(2011, 5, 17, 23, 59, 59.9999999, -7, 0)`
