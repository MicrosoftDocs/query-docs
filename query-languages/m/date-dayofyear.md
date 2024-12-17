---
description: "Learn more about: Date.DayOfYear"
title: "Date.DayOfYear"
ms.subservice: m-source
---
# Date.DayOfYear

## Syntax

<pre>
Date.DayOfYear(<b>dateTime</b> as any) as nullable number
</pre>
  
## About

Returns a number representing the day of the year in the provided `date`, `datetime`, or `datetimezone` value, `dateTime`.

## Example 1

The day of the year for March 1st, 2011.

**Usage**

```powerquery-m
Date.DayOfYear(#date(2011, 03, 01))
```

**Output**

`60`
