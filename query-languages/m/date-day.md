---
description: "Learn more about: Date.Day"
title: "Date.Day"
---
# Date.Day

## Syntax

<pre>
Date.Day(<b>dateTime</b> as any) as nullable number
</pre>

## About

Returns the day component of a `date`, `datetime`, or `datetimezone` value.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value from which the day component is extracted.

## Example 1

Get the day component of a `date`, `datetime`, or `datetimezone` value representing the date and time of 5/14/2011 05:00:00 PM.

**Usage**

```powerquery-m
Date.Day(#datetime(2011, 5, 14, 17, 0, 0))
```

**Output**

`14`
