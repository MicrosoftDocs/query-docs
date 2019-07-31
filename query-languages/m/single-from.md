---
title: "Single.From | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Single.From

## Syntax

<pre>
Single.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number 
</pre>
  
## About  
Returns a Single `number` value from the given `value`. If the given `value` is `null`, `Single.From` returns `null`. If the given `value` is `number` within the range of Single, `value` is returned, otherwise an error is returned. If the given `value` is of any other type, see `Number.FromText` for converting it to `number` value, then the previous statement about converting `number` value to Single `number` value applies.

## Example 1
Get the Single `number` value of `"1.5"`.

```powerquery-m
Single.From("1.5")
```

`1.5`
