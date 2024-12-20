---
description: "Learn more about: Date.IsLeapYear"
title: "Date.IsLeapYear"
ms.subservice: m-source
---
# Date.IsLeapYear

## Syntax

<pre>  
Date.IsLeapYear(<b>dateTime</b> as any) as nullable logical 
</pre>
  
## About

Indicates whether the given datetime value `dateTime` falls in is a leap year.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the year 2012, as represented by `#date(2012, 01, 01)` is a leap year.

**Usage**

```powerquery-m
Date.IsLeapYear(#date(2012, 01, 01))
```

**Output**

`true`
