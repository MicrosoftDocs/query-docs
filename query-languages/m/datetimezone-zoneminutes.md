---
description: "Learn more about: DateTimeZone.ZoneMinutes"
title: "DateTimeZone.ZoneMinutes"
ms.subservice: m-source
ms.topic: reference
---
# DateTimeZone.ZoneMinutes

## Syntax

<pre>
DateTimeZone.ZoneMinutes(<b>dateTimeZone</b> as nullable datetimezone) as nullable number
</pre>

## About

Returns the time zone minutes component of a `datetimezone` value.

* `dateTimeZone`: a `datetimezone` value from which the time zone minutes component is extracted. If `dateTimeZone` is `null`, the function returns `null`.

## Example 1

Get the time zone minutes component of the specified `datetimezone` value.

**Usage**

```powerquery-m
DateTimeZone.ZoneMinutes(#datetimezone(2024, 4, 28, 13, 24, 22, 7, 30))
```

**Output**

`30`
