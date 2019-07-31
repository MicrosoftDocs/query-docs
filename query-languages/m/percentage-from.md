---
title: "Percentage.From | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Percentage.From

## Syntax

<pre>
Percentage.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About
Returns a `percentage` value from the given `value`. If the given `value` is `null`, `Percentage.From` returns `null`. If the given `value` is `text` with a trailing percent symbol, then the converted decimal number will be returned. Otherwise, see `Number.From` for converting it to `number` value.

## Example 1
Get the `percentage` value of `"12.3%"`.

```powerquery-m
Percentage.From("12.3%")
```

`0.123`
