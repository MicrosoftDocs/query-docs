---
description: "Learn more about: Single.From"
title: "Single.From | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Single.From

## Syntax

<pre>
Single.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>
  
## About

Returns a Single `number` value from the given `value`. If the given `value` is `null`, **Single.From** returns `null`. If the given `value` is `number` within the range of Single, `value` is returned, otherwise an error is returned. If `value` is of any other type, it will first be converted to a `number` using [Number.FromText](/powerquery-m/number-fromtext). An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the Single `number` value of `"1.5"`.

**Usage**

```powerquery-m
Single.From("1.5")
```

**Output**

`1.5`
