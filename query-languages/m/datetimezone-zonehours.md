---
description: "Learn more about: DateTimeZone.ZoneHours"
title: "DateTimeZone.ZoneHours"
ms.subservice: m-source
ms.topic: reference
---
# DateTimeZone.ZoneHours

## Syntax

<pre>
DateTimeZone.ZoneHours(<b>dateTimeZone</b> as nullable datetimezone) as nullable number
</pre>

## About

Returns the time zone hour component of a `datetimezone` value.

* `dateTimeZone`: A `datetimezone` value from which the time zone hour component is extracted. If `dateTimeZone` is `null`, the function returns `null`.

## Example 1

Get the time zone hours component of the specified `datetimezone` value.

**Usage**

```powerquery-m
DateTimeZone.ZoneHours(#datetimezone(2024, 4, 28, 13, 24, 22, 7, 30))
```

**Output**

`7`
