---
description: "Learn more about: Date.IsInNextQuarter"
title: "Date.IsInNextQuarter"
ms.subservice: m-source
---
# Date.IsInNextQuarter

## Syntax

<pre>
Date.IsInNextQuarter(<b>dateTime</b> as any) as nullable logical
</pre>  

## About

Indicates whether the given datetime value `dateTime` occurs during the next quarter, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current quarter.

* `dateTime`: A `date`, `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the quarter after the current system time is in the next quarter.

**Usage**

```powerquery-m
Date.IsInNextQuarter(Date.AddQuarters(DateTime.FixedLocalNow(), 1))
```

**Output**

`true`
