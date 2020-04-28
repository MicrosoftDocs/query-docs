---
title: "Int16.From | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Int16.From

## Syntax

<pre>
Int16.From(<b>value</b> as any, optional <b>culture</b> as nullable text, optional <b>roundingMode</b> as nullable number) as nullable number
</pre>
  
## About  
Returns a 16-bit integer `number` value from the given `value`. If the given `value` is `null`, `Int16.From` returns `null`. If the given `value` is `number` within the range of 16-bit integer without a fractional part, `value` is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is `RoundingMode.ToEven`. If the given `value` is of any other type, see `Number.FromText` for converting it to `number` value, then the previous statement about converting `number` value to 16-bit integer `number` value applies. See `Number.Round` for the available rounding modes. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get the 16-bit integer `number` value of `"4"`.

```powerquery-m
Int64.From("4")
```

`4`

## Example 2
Get the 16-bit integer `number` value of `"4.5"` using `RoundingMode.AwayFromZero`.

```powerquery-m
Int16.From("4.5", null, RoundingMode.AwayFromZero)
```

`5`
