---
title: "Decimal.From | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Decimal.From

## Syntax

<pre>
Decimal.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number 
</pre>
  
## About  
Returns a Decimal `number` value from the given `value`. If the given `value` is `null`, `Decimal.From` returns `null`. If the given `value` is `number` within the range of Decimal, `value` is returned, otherwise an error is returned. If the given `value` is of any other type, see `Number.FromText` for converting it to `number` value, then the previous statement about converting `number` value to Decimal `number` value applies.

## Example 1
Get the Decimal `number` value of `"4.5"`.

```powerquery-m
Decimal.From("4.5")
```

`4.5`
