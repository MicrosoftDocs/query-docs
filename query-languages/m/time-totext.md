---
description: "Learn more about: Time.ToText"
title: "Time.ToText"
---
# Time.ToText

## Syntax

<pre>
Time.ToText(<b>time</b> as nullable time, optional <b>options</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>

## About

Returns a textual representation of `time`. An optional `record` parameter, `options`, may be provided to specify additional properties. `culture` is only used for legacy workflows. The `record` can contain the following fields:

* `Format`: A `text` value indicating the format to use. For more details, go to [Standard date and time format strings](standard-date-and-time-format-strings.md) and [Custom date and time format strings](custom-date-and-time-format-strings.md). Omitting this field or providing `null` will result in formatting the date using the default defined by `Culture`.

* `Culture`: When `Format` is not null, `Culture` controls some format specifiers. For example, in `"en-US"` `"tt"` is `"AM" or "PM"`, while in `"ar-EG"` `"tt"` is `"ص" or "م"`. When `Format` is `null`, `Culture` controls the default format to use. When `Culture` is `null` or omitted, [Culture.Current](culture-current.md) is used.

To support legacy workflows, `options` and `culture` may also be text values. This has the same behavior as if `options = [Format = options, Culture = culture]`.

## Example 1

Convert `#time(01, 30, 25)` into a `text` value. *Result output may vary depending on current culture.*

**Usage**

```powerquery-m
Time.ToText(#time(11, 56, 2))
```

**Output**

`"11:56 AM"`

## Example 2

Convert using a custom format and the German culture.

**Usage**

```powerquery-m
Time.ToText(#time(11, 56, 2), [Format="hh:mm", Culture="de-DE"])
```

**Output**

`"11:56"`

## Example 3

Convert using standard time format.

**Usage**

```powerquery-m
Time.ToText(#time(11, 56, 2), [Format="T", Culture="de-DE"])
```

**Output**

`"11:56:02"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
