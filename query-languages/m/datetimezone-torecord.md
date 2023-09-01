---
description: "Learn more about: DateTimeZone.ToRecord"
title: "DateTimeZone.ToRecord"
---
# DateTimeZone.ToRecord

## Syntax

<pre>
DateTimeZone.ToRecord(<b>dateTimeZone</b> as datetimezone) as record
</pre>
  
## About

Returns a record containing the parts of the given datetimezone value, `dateTimeZone`.

* `dateTimeZone`: A `datetimezone` value for from which the record of its parts is to be calculated.

## Example 1

Convert the `#datetimezone(2011, 12, 31, 11, 56, 2, 8, 0)` value into a record containing Date, Time, and Zone values.

**Usage**

```powerquery-m
DateTimeZone.ToRecord(#datetimezone(2011, 12, 31, 11, 56, 2, 8, 0))
```

**Output**

```powerquery-m
[
      Year = 2011,
      Month = 12,
      Day = 31,
      Hour = 11,
      Minute = 56,
      Second = 2,
      ZoneHours = 8,
      ZoneMinutes = 0
]
```
