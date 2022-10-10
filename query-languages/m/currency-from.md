---
description: "Learn more about: Currency.From"
title: "Currency.From"
ms.date: 10/7/2022
---
# Currency.From

## Syntax

<pre> 
Currency.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>

## About

Returns a `currency` value from the given `value`. If the given `value` is `null`, **Currency.From** returns `null`. If the given `value` is `number` within the range of currency, fractional part of the `value` is rounded to 4 decimal digits and returned. If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](number-fromtext.md). Valid range for currency is `-922,337,203,685,477.5808` to `922,337,203,685,477.5807`. Refer to [Number.Round](number-round.md) for the available rounding modes. The default is [RoundingMode.ToEven](roundingmode-type.md). An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the `currency` value of `"1.23455"`.

**Usage**

```powerquery-m
Currency.From("1.23455")
```

**Output**

`1.2346`

## Example 2

Get the `currency` value of `"1.23455"` using `RoundingMode.Down`.

**Usage**

```powerquery-m
Currency.From("1.23455", "en-US", RoundingMode.Down)
```

**Output**

`1.2345`
