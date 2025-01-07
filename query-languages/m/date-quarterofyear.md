---
description: "Learn more about: Date.QuarterOfYear"
title: "Date.QuarterOfYear"
ms.subservice: m-source
---
# Date.QuarterOfYear

## Syntax

<pre>
Date.QuarterOfYear(<b>dateTime</b> as any) as nullable number
</pre>
  
## About

Returns a number from 1 to 4 indicating which quarter of the year the date `dateTime` falls in. `dateTime` can be a `date`, `datetime`, or `datetimezone` value.

## Example 1

Find which quarter of the year the date #date(2011, 12, 31) falls in.

**Usage**

```powerquery-m
Date.QuarterOfYear(#date(2011, 12, 31))
```

**Output**

`4`
