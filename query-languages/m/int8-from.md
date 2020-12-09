---
title: "Int8.From | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Int8.From

## Syntax

<pre>
Int8.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>
  
## About  
Returns a signed 8-bit integer `number` value from the given `value`. If the given `value` is `null`, `Int8.From` returns `null`. If the given `value` is `number` within the range of signed 8-bit integer without a fractional part, `value` is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is `RoundingMode.ToEven`. If the given `value` is of any other type, see `Number.FromText` for converting it to `number` value, then the previous statement about converting `number` value to signed 8-bit integer `number` value applies. See `Number.Round` for the available rounding modes. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get the signed 8-bit integer `number` value of `"4"`.

```powerquery-m
Int8.From("4")
```

`4`

## Example 2
Get the signed 8-bit integer `number` value of `"4.5"` using `RoundingMode.AwayFromZero`.

```powerquery-m
Int8.From("4.5", null, RoundingMode.AwayFromZero)
```

`5`

