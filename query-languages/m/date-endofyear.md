---
description: "Learn more about: Date.EndOfYear"
title: "Date.EndOfYear"
ms.date: 11/14/2022
---
# Date.EndOfYear

## Syntax

<pre>
Date.EndOfYear(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the end of the year that contains `dateTime`, including fractional seconds. Time zone information is preserved.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the end of the year is calculated.

## Example 1

Get the end of the year for 5/14/2011 05:00:00 PM.

**Usage**

```powerquery-m
Date.EndOfYear(#datetime(2011, 5, 14, 17, 0, 0))
```

**Output**

`#datetime(2011, 12, 31, 23, 59, 59.9999999)`

## Example 2

Get the end of hour for 5/17/2011 05:00:00 PM -7:00.

**Usage**

```powerquery-m
Date.EndOfYear(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

**Output**

`#datetimezone(2011, 12, 31, 23, 59, 59.9999999, -7, 0)`
