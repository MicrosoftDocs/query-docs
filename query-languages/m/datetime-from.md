---
description: "Learn more about: DateTime.From"
title: "DateTime.From"
ms.subservice: m-source
ms.topic: reference
---
# DateTime.From

## Syntax

<pre>
DateTime.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable datetime
</pre>
  
## About

Returns a `datetime` value from the given `value`. An optional `culture` may also be provided (for example, "en-US"). If the given `value` is `null`, **DateTime.From** returns `null`. If the given `value` is `datetime`, `value` is returned. Values of the following types can be converted to a `datetime` value:

* `text`: A `datetime` value from textual representation. Refer to [DateTime.FromText](datetime-fromtext.md) for details.
* `date`: A `datetime` with `value` as the date component and `12:00:00 AM` as the time component.
* `datetimezone`: The local `datetime` equivalent of `value`.
* `time`: A `datetime` with the date equivalent of the OLE Automation Date of `0` as the date component and `value` as the time component.
* `number`: A `datetime` equivalent of the OLE Automation Date expressed by `value`.

If `value` is of any other type, an error is returned.

## Example 1

Convert `#time(06, 45, 12)` to a `datetime` value.

**Usage**

```powerquery-m
DateTime.From(#time(06, 45, 12))
```

**Output**

`#datetime(1899, 12, 30, 06, 45, 12)`

## Example 2

Convert `#date(1975, 4, 4)` to a `datetime` value.

**Usage**

```powerquery-m
DateTime.From(#date(1975, 4, 4))
```

**Output**

`#datetime(1975, 4, 4, 0, 0, 0)`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
