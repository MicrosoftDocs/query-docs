---
description: "Learn more about: Time.From"
title: "Time.From"
---
# Time.From

## Syntax

<pre> 
Time.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable time
</pre>
  
## About

Returns a `time` value from the given `value`. An optional `culture` may also be provided (for example, "en-US"). If the given `value` is `null`, **Time.From** returns `null`. If the given `value` is `time`, `value` is returned. Values of the following types can be converted to a `time` value:

* `text`: A `time` value from textual representation. Refer to [Time.FromText](time-fromtext.md) for details.
* `datetime`: The time component of the `value`.
* `datetimezone`: The time component of the local datetime equivalent of `value`.
* `number`: A `time` equivalent to the number of fractional days expressed by `value`. If `value` is negative or greater or equal to 1, an error is returned.

If `value` is of any other type, an error is returned.

## Example 1

Convert `0.7575` to a `time` value.

**Usage**

```powerquery-m
Time.From(0.7575)
```

**Output**

`#time(18, 10, 48)`

## Example 2

Convert `#datetime(1899, 12, 30, 06, 45, 12)` to a `time` value.

**Usage**

```powerquery-m
Time.From(#datetime(1899, 12, 30, 06, 45, 12))
```

**Output**

`#time(06, 45, 12)`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)