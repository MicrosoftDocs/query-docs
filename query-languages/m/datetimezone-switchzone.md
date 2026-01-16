---
description: "Learn more about: DateTimeZone.SwitchZone"
title: "DateTimeZone.SwitchZone"
ms.subservice: m-source
---
# DateTimeZone.SwitchZone

## Syntax

<pre>
DateTimeZone.SwitchZone(<b>dateTimeZone</b> as nullable datetimezone, <b>timezoneHours</b> as number, optional <b>timezoneMinutes</b> as nullable number) as nullable datetimezone
</pre>
  
## About

Changes timezone information to on the datetimezone value `dateTimeZone` to the new timezone information provided by `timezoneHours` and optionally `timezoneMinutes`. If `dateTimeZone` does not have a timezone component, an error is raised.

## Example 1

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to 8 hours.

**Usage**

```powerquery-m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30), 8)
```

**Output**

`#datetimezone(2010, 12, 31, 12, 26, 2, 8, 0)`

## Example 2

Change timezone information for #datetimezone(2010, 12, 31, 11, 56, 02, 7, 30) to -30 minutes.

**Usage**

```powerquery-m
DateTimeZone.SwitchZone(#datetimezone(2010, 12, 31, 11, 56, 02, 7, 30), 0, -30)
```

**Output**

`#datetimezone(2010, 12, 31, 3, 56, 2, 0, -30)`
