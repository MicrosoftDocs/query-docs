---
description: "Learn more about: Byte.From"
title: "Byte.From"
---
# Byte.From

## Syntax

<pre>
Byte.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>

## About

Returns an 8-bit integer `number` value from the given `value`. If the given `value` is `null`, **Byte.From** returns `null`. If the given `value` is a `number` within the range of an 8-bit integer without a fractional part, `value` is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is [RoundingMode.ToEven](roundingmode-type.md). If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](number-fromtext.md). Refer to [Number.Round](number-round.md) for the available rounding modes. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the 8-bit integer `number` value of `"4"`.

**Usage**

```powerquery-m
Byte.From("4")
```

**Output**

`4`

## Example 2

Get the 8-bit integer `number` value of `"4.5"` using [RoundingMode.AwayFromZero](roundingmode-type.md).

**Usage**

```powerquery-m
Byte.From("4.5", null, RoundingMode.AwayFromZero)
```

**Output**

`5`
