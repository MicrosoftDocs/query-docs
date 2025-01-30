---
description: "Learn more about: DateTimeZone.ToText"
title: "DateTimeZone.ToText"
ms.subservice: m-source
---
# DateTimeZone.ToText

## Syntax

<pre>
DateTimeZone.ToText(<b>dateTimeZone</b> as nullable datetimezone, optional <b>options</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Returns a textual representation of `dateTimeZone`. An optional `record` parameter, `options`, may be provided to specify additional properties. `culture` is only used for legacy workflows. The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. For more details, go to * [Standard date and time format strings](standard-date-and-time-format-strings.md) and [Custom date and time format strings](custom-date-and-time-format-strings.md). Omitting this field or providing `null` will result in formatting the date using the default defined by `Culture`.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"MMM"` is `"Jan", "Feb", "Mar", ...`, while in `"ru-RU"` `"MMM"` is `"янв", "фев", "мар", ...`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` and `culture` may also be text values. This has the same behavior as if `options = [Format = options, Culture = culture]`.

## Example 1

Convert `#datetimezone(2010, 12, 31, 01, 30, 25, 2, 0)` into a `text` value. *Result output may vary depending on current culture.*

**Usage**

```powerquery-m
DateTimeZone.ToText(#datetimezone(2010, 12, 31, 01, 30, 25, 2, 0))
```

**Output**

`"12/31/2010 1:30:25 AM +02:00"`

## Example 2

Convert using a custom format and the German culture.

**Usage**

```powerquery-m
DateTimeZone.ToText(#datetimezone(2010, 12, 30, 2, 4, 50.36973, -8,0), [Format="dd MMM yyyy HH:mm:ss.ffffff zzz", Culture="de-DE"])
```

**Output**

`"30 Dez 2010 02:04:50.369730 -08:00"`

## Example 3

Convert using the ISO 8601 pattern.

**Usage**

```powerquery-m
DateTimeZone.ToText(#datetimezone(2000, 2, 8, 3, 45, 12, 2, 0),[Format="O", Culture="en-US"])
```

**Output**

`"2000-02-08T03:45:12.0000000+02:00"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
