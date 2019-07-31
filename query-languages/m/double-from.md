---
title: "Double.From | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Double.From

## Syntax

<pre>
Double.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>
  
## About  
Returns a Double `number` value from the given `value`. If the given `value` is `null`, `Double.From` returns `null`. If the given `value` is `number` within the range of Double, `value` is returned, otherwise an error is returned. If the given `value` is of any other type, see `Number.FromText` for converting it to `number` value, then the previous statement about converting `number` value to Double `number` value applies.

## Example 1
Get the Double `number` value of `"4"`.

```powerquery-m
Double.From("4.5")
```

`4.5`
