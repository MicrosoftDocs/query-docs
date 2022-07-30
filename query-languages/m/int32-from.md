---
description: "Learn more about: Int32.From"
title: "Int32.From | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Int32.From

## Syntax

<pre>
Int32.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>
  
## About

Returns a 32-bit integer `number` value from the given `value`. If the given `value` is `null`, **Int32.From** returns `null`. If the given `value` is `number` within the range of 32-bit integer without a fractional part, `value` is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is [RoundingMode.ToEven](/powerquery-m/roundingmode-toeven). If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](/powerquery-m/number-fromtext). Refer to [Number.Round](/powerquery-m/number-round) for the available rounding modes. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the 32-bit integer `number` value of `"4"`.

**Usage**

```powerquery-m
Int32.From("4")
```

**Output**

`4`

## Example 2

Get the 32-bit integer `number` value of `"4.5"` using `RoundingMode.AwayFromZero`.

**Usage**

```powerquery-m
Int32.From("4.5", null, RoundingMode.AwayFromZero)
```

**Output**

`5`
