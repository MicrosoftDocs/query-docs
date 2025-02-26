---
description: "Learn more about: DateTime.IsInCurrentHour"
title: "DateTime.IsInCurrentHour"
ms.subservice: m-source
---
# DateTime.IsInCurrentHour

## Syntax

<pre>
DateTime.IsInCurrentHour(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About

Indicates whether the given datetime value `dateTime` occurs during the current hour, as determined by the current date and time on the system.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current hour.

**Usage**

```powerquery-m
DateTime.IsInCurrentHour(DateTime.FixedLocalNow())
```

**Output**

`true`

