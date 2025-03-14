---
description: "Learn more about: Int64.From"
title: "Int64.From"
ms.subservice: m-source
---
# Int64.From

## Syntax

<pre>
Int64.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>

## About

Returns a 64-bit integer `number` value from the given `value`. If the given `value` is `null`, **Int64.From** returns `null`. If the given `value` is `number` within the range of 64-bit integer without a fractional part, `value` is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is [RoundingMode.ToEven](roundingmode-type.md). If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](number-fromtext.md). Refer to [Number.Round](number-round.md) for the available rounding modes. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the 64-bit integer `number` value of `"4"`.

**Usage**

```powerquery-m
Int64.From("4")
```

**Output**

`4`

## Example 2

Get the 64-bit integer `number` value of `"4.5"` using `RoundingMode.AwayFromZero`.

**Usage**

```powerquery-m
Int64.From("4.5", null, RoundingMode.AwayFromZero)
```

**Output**

`5`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
