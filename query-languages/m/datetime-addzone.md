---
description: "Learn more about: DateTime.AddZone"
title: "DateTime.AddZone"
ms.date: 3/11/2022
---
# DateTime.AddZone

## Syntax

<pre>
DateTime.AddZone(<b>dateTime</b> as nullable datetime, <b>timezoneHours</b> as number, optional <b>timezoneMinutes</b> as nullable number) as nullable datetimezone
</pre>
  
## About

Sets timezone information to on the datetime value `dateTime`. The timezone information will include `timezoneHours` and optionally `timezoneMinutes`.

## Example 1

Set timezone information for #datetime(2010, 12, 31, 11, 56, 02) to 7 hours, 30 minutes.

**Usage**

```powerquery-m
DateTime.AddZone(#datetime(2010, 12, 31, 11, 56, 02), 7, 30)
```

**Output**

`#datetimezone(2010, 12, 31, 11, 56, 2, 7, 30)`
