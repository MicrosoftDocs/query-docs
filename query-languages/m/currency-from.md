---
description: "Learn more about: Currency.From"
title: "Currency.From | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Currency.From

## Syntax

<pre> 
Currency.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>
  
## About  
Returns a `currency` value from the given `value`. If the given `value` is `null`, `Currency.From` returns `null`. If the given `value` is `number` within the range of currency, fractional part of the `value` is rounded to 4 decimal digits and returned. If the given `value` is of any other type, see `Number.FromText` for converting it to `number` value, then the previous statement about converting `number` value to `currency` value applies. Valid range for currency is `-922,337,203,685,477.5808` to `922,337,203,685,477.5807`. See `Number.Round` for the available rounding modes. The default is `RoundingMode.ToEven`. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get the `currency` value of `"1.23455"`.

```powerquery-m
Currency.From("1.23455")
```

`1.2346`

## Example 2
Get the `currency` value of `"1.23455"` using `RoundingMode.Down`.

```powerquery-m
Currency.From("1.23455", "en-Us", RoundingMode.Down)
```

`1.2345`
