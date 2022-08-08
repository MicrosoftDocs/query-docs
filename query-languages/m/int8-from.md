---
description: "Learn more about: Int8.From"
title: "Int8.From"
ms.date: 4/13/2022
---
# Int8.From

## Syntax

<pre>
Int8.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>
  
## About

Returns a signed 8-bit integer `number` value from the given `value`. If the given `value` is `null`, **Int8.From** returns `null`. If the given `value` is `number` within the range of signed 8-bit integer without a fractional part, `value` is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is [RoundingMode.ToEven](/powerquery-m/roundingmode-toeven). If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](/powerquery-m/number-fromtext). Refer to [Number.Round](/powerquery-m/number-round) for the available rounding modes. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the signed 8-bit integer `number` value of `"4"`.

**Usage**

```powerquery-m
Int8.From("4")
```

**Output**

`4`

## Example 2

Get the signed 8-bit integer `number` value of `"4.5"` using [RoundingMode.AwayFromZero](/powerquery-m/roundingmode-awayfromzero).

**Usage**

```powerquery-m
Int8.From("4.5", null, RoundingMode.AwayFromZero)
```

**Output**

`5`
