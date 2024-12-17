---
description: "Learn more about: DateTime.AddZone"
title: "DateTime.AddZone"
ms.subservice: m-source
---
# DateTime.AddZone

## Syntax

<pre>
DateTime.AddZone(<b>dateTime</b> as nullable datetime, <b>timezoneHours</b> as number, optional <b>timezoneMinutes</b> as nullable number) as nullable datetimezone
</pre>
  
## About

Adds timezone information to the `dateTime` value. The timezone information includes `timezoneHours` and optionally `timezoneMinutes`, which specify the desired offset from UTC time.

## Example 1

Set the timezone to UTC+7:30 (7 hours and 30 minutes past UTC).

**Usage**

```powerquery-m
DateTime.AddZone(#datetime(2010, 12, 31, 11, 56, 02), 7, 30)
```

**Output**

`#datetimezone(2010, 12, 31, 11, 56, 2, 7, 30)`
