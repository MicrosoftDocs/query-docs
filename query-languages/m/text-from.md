---
description: "Learn more about: Text.From"
title: "Text.From"
---
# Text.From

## Syntax

<pre>
Text.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Returns the text representation of `value`. The `value` can be a `number`, `date`, `time`, `datetime`, `datetimezone`, `logical`, `duration` or `binary` value. If the given value is null, `Text.From` returns null. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Create a text value from the number 3.

**Usage**

```powerquery-m
Text.From(3)
```

**Output**

`"3"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
* [Standard numeric format strings](standard-numeric-format-strings.md)
* [Custom numeric format strings](custom-numeric-format-strings.md)
* [Standard date and time format strings](standard-date-and-time-format-strings.md)
* [Custom date and time format strings](custom-date-and-time-format-strings.md)
