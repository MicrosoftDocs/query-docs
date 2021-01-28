---
description: "Learn more about: Percentage.From"
title: "Percentage.From | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Percentage.From

## Syntax

<pre>
Percentage.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About
Returns a `percentage` value from the given `value`. If the given `value` is `null`, `Percentage.From` returns `null`. If the given `value` is `text` with a trailing percent symbol, then the converted decimal number will be returned. Otherwise, see `Number.From` for converting it to `number` value. An optional `culture` may also be provided (for example, "en-US").

## Example 1
Get the `percentage` value of `"12.3%"`.

```powerquery-m
Percentage.From("12.3%")
```

`0.123`
