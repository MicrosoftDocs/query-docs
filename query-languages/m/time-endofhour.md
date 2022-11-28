---
description: "Learn more about: Time.EndOfHour"
title: "Time.EndOfHour"
ms.date: 11/14/2022
---
# Time.EndOfHour

## Syntax

<pre>
Time.EndOfHour(<b>dateTime</b> as any) as any
</pre>
  
## About

Returns the end of the hour represented by `dateTime`, including fractional seconds. Time zone information is preserved.

* `dateTime`: A `time`, `datetime`, or `datetimezone` value from which the end of the hour is calculated.

## Example 1

Get the end of the hour for 5/14/2011 05:00:00 PM.

**Usage**

```powerquery-m
Time.EndOfHour(#datetime(2011, 5, 14, 17, 0, 0))
```

**Output**

`#datetime(2011, 5, 14, 17, 59, 59.9999999)`

## Example 2

Get the end of the hour for 5/17/2011 05:00:00 PM -7:00.

**Usage**

```powerquery-m
Time.EndOfHour(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0))
```

**Output**

`#datetimezone(2011, 5, 17, 5, 59, 59.9999999, -7, 0)`
