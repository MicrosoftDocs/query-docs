---
description: "Learn more about: Date.EndOfMonth"
title: "Date.EndOfMonth"
ms.date: 3/11/2022
---
# Date.EndOfMonth

## Syntax

<pre>
Date.EndOfMonth(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the last day of the month in `dateTime`.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the end of the month is calculated

## Example 1

Get the end of the month for 5/14/2011.

**Usage**

```powerquery-m
Date.EndOfMonth(#date(2011, 5, 14))
```

**Output**

`#date(2011, 5, 31)`

## Example 2

Get the end of the month for 5/17/2011 05:00:00 PM -7:00.

**Usage**

```powerquery-m
Date.EndOfMonth(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

**Output**

`#datetimezone(2011, 5, 31, 23, 59, 59.9999999, -7, 0)`
