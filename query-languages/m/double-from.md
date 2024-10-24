---
description: "Learn more about: Double.From"
title: "Double.From"
---
# Double.From

## Syntax

<pre>
Double.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About

Returns a Double `number` value from the given `value`. If the given `value` is `null`, **Double.From** returns `null`. If the given `value` is `number` within the range of Double, `value` is returned, otherwise an error is returned. If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](number-fromtext.md). An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the Double `number` value of `"4"`.

**Usage**

```powerquery-m
Double.From("4.5")
```

**Output**

`4.5`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
