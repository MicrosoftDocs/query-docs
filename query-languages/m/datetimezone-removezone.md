---
description: "Learn more about: DateTimeZone.RemoveZone"
title: "DateTimeZone.RemoveZone"
ms.date: 3/11/2022
---
# DateTimeZone.RemoveZone

## Syntax

<pre>
DateTimeZone.RemoveZone(<b>dateTimeZone</b> as nullable datetimezone) as nullable datetime
</pre>
  
## About

Returns a #datetime value from `dateTimeZone` with timezone information removed.

## Example 1

Remove timezone information from the value #datetimezone(2011, 12, 31, 9, 15, 36, -7, 0).

**Usage**

```powerquery-m
DateTimeZone.RemoveZone(#datetimezone(2011, 12, 31, 9, 15, 36, -7, 0))
```

**Output**

`#datetime(2011, 12, 31, 9, 15, 36)`
