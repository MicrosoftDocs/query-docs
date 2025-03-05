---
description: "Learn more about: DateTime.IsInCurrentMinute"
title: "DateTime.IsInCurrentMinute"
ms.subservice: m-source
---
# DateTime.IsInCurrentMinute

## Syntax

<pre>
DateTime.IsInCurrentMinute(<b>dateTime</b> as any) as nullable logical
</pre>
  
## About
Indicates whether the given datetime value `dateTime` occurs during the current minute, as determined by the current date and time on the system.

* `dateTime`: A `datetime`, or `datetimezone` value to be evaluated.

## Example 1

Determine if the current system time is in the current minute.

**Usage**

```powerquery-m
DateTime.IsInCurrentMinute(DateTime.FixedLocalNow())
```

**Output**

`true`
