---
description: "Learn more about: DateTimeZone.From"
title: "DateTimeZone.From"
ms.subservice: m-source
---
# DateTimeZone.From

## Syntax

<pre>
DateTimeZone.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable datetimezone
</pre>
  
## About

Creates a `datetimezone` from the given value.

* `value`: The value used to create a `datetimezone`.
* `culture`: (Optional) The culture to use when transforming the value (for example, "en-US").

Values of the following types can be converted to a `datetimezone` value:

* `text`: Returns a `datetimezone` value from textual representation. Refer to [DateTimeZone.FromText](datetimezone-fromtext.md) for details.
* `date`: Returns a `datetimezone` with `value` as the date component, `12:00:00 AM` as the time component, and the offset corresponding the local time zone.
* `datetime`: Returns a `datetimezone` with `value` as the datetime and the offset corresponding the local time zone.
* `datetimezone`: Returns `value`.
* `time`: Returns a `datetimezone` with the date equivalent of the OLE Automation Date of `0` as the date component, `value` as the time component, and the offset corresponding the local time zone. The OLE Automation Date consists of a floating-point number whose integral component is the number of days before or after midnight, 30 December 1899, and whose fractional component represents the time on that day divided by 24. For example, midnight, 31 December 1899 is represented by 1.0; 6 A.M., 1 January 1900 is represented by 2.25; midnight, 29 December 1899 is represented by -1.0; and 6 A.M., 29 December 1899 is represented by -1.25. The base value is midnight, 30 December 1899. The minimum value is midnight, 1 January 0100. The maximum value is the last moment of 31 December 9999.
* `number`: Returns a `datetimezone` with the datetime equivalent to the OLE Automation Date expressed by `value` and the offset corresponding the local time zone.
* `null`: Returns `null`.

If `value` is of any other type, an error is returned.

The value of the offset corresponding to the local time zone is different when running this function locally as opposed to running it online. When run locally, the local time zone is returned. When run online, the UTC time zone (+00:00) is returned.

## Example 1

Convert the textual representation of a date, time, and timezone to a 'datetimezone` value.

**Usage**

```powerquery-m
DateTimeZone.From("2020-10-30T01:30:00-08:00")
```

**Output**

`#datetimezone(2020, 10, 30, 01, 30, 00, -8, 00)`

## Example 2

Convert the textual representation of Brazilian Portuguese date, time, and timezone to a `datetimezone` value.

**Usage**

```powerquery-m
DateTimeZone.From("13 de agosto de 2025 15:43:00 -03:00", "pt-BR")
```

**Output**

`#datetimezone(2025, 08, 13, 03, 43, 00, -3, 00)`

## Example 3

Convert a number representing January 1, 2025 at 12 PM to a `datetimezone` value.

**Usage**

```powerquery-m
DateTimeZone.From(45658.5)
```

**Output**

`#datetimezone(2025, 01, 01, 12, 00, 00, 0, 00)`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Local, fixed, and UTC variants of current time functions](m-local-fixed-utc-variants.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
* [Number.From](number-from.md)
