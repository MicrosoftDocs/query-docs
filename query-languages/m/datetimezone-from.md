---
description: "Learn more about: DateTimeZone.From"
title: "DateTimeZone.From | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: dougklo
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# DateTimeZone.From

## Syntax

<pre>
DateTimeZone.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable datetimezone
</pre>
  
## About

Returns a `datetimezone` value from the given `value`. An optional `culture` may also be provided (for example, "en-US"). If the given `value` is `null`, `DateTimeZone.From` returns `null`. If the given `value` is `datetimezone`, `value` is returned. Values of the following types can be converted to a `datetimezone` value:

* `text`: A `datetimezone` value from textual representation. Go to [DateTimeZone.FromText](datetimezone-fromtext.md) for details.
* `date`: A `datetimezone` with `value` as the date component, `12:00:00 AM` as the time component and the offset corresponding the local time zone.
* `datetime`: A `datetimezone` with `value` as the datetime and the offset corresponding the local time zone.
* `time`: A `datetimezone` with the date equivalent of the OLE Automation Date of `0` as the date component, `value` as the time component and the offset corresponding the local time zone.
* `number`: A `datetimezone` with the datetime equivalent to the OLE Automation Date expressed by `value` and the offset corresponding the local time zone.

If `value` is of any other type, an error is returned.

## Example 1

Convert `"2020-10-30T01:30:00-08:00"` to a `datetimezone` value.

**Usage**

```powerquery-m
DateTimeZone.From("2020-10-30T01:30:00-08:00")
```

**Output**

`#datetimezone(2020, 10, 30, 01, 30, 00, -8, 00)`
