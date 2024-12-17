---
description: "Learn more about: Number.From"
title: "Number.From"
ms.subservice: m-source
---
# Number.From

## Syntax

<pre>
Number.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About

Returns a `number` value from the given `value`. An optional `culture` may also be provided (for example, "en-US"). If the given `value` is `null`, **Number.From** returns `null`. If the given `value` is `number`, `value` is returned. Values of the following types can be converted to a `number` value:

* `text`: A `number` value from textual representation. Common text formats are handled ("15", "3,423.10", "5.0E-10"). Refer to [Number.FromText](/powerquery-m/number-fromtext) for details.
* `logical`: 1 for `true`, 0 for `false`.
* `datetime`: A double-precision floating-point number that contains an OLE Automation date equivalent.
* `datetimezone`: A double-precision floating-point number that contains an OLE Automation date equivalent of the local date and time of `value`.
* `date`: A double-precision floating-point number that contains an OLE Automation date equivalent.
* `time`: Expressed in fractional days.
* `duration`: Expressed in whole and fractional days.

If `value` is of any other type, an error is returned.

## Example 1

Get the `number` value of `"4"`.

**Usage**

```powerquery-m
Number.From("4")
```

**Output**

`4`

## Example 2

Get the `number` value of `#datetime(2020, 3, 20, 6, 0, 0)`.

**Usage**

```powerquery-m
Number.From(#datetime(2020, 3, 20, 6, 0, 0))
```

**Output**

`43910.25`

## Example 3

Get the `number` value of `"12.3%"`.

**Usage**

```powerquery-m
Number.From("12.3%")
```

**Output**

`0.123`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard numeric format strings](standard-numeric-format-strings.md)
* [Custom numeric format strings](custom-numeric-format-strings.md)
