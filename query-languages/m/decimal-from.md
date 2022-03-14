---
description: "Learn more about: Decimal.From"
title: "Decimal.From | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Decimal.From

## Syntax

<pre>
Decimal.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>
  
## About

Returns a Decimal `number` value from the given `value`. If the given `value` is `null`, `Decimal.From` returns `null`. If the given `value` is `number` within the range of Decimal, `value` is returned, otherwise an error is returned. If the given `value` is of any other type, see [Number.FromText](/powerquery-m/number-fromtext) for converting it to `number` value, then the previous statement about converting `number` value to Decimal `number` value applies. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the Decimal `number` value of `"4.5"`.

**Usage**

```powerquery-m
Decimal.From("4.5")
```

**Output**

`4.5`
