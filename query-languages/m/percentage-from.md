---
description: "Learn more about: Percentage.From"
title: "Percentage.From | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Percentage.From

## Syntax

<pre>
Percentage.From(<b>value</b> as any, optional <b>culture</b> as nullable text) as nullable number
</pre>

## About

Returns a `percentage` value from the given `value`. If the given `value` is `null`, **Percentage.From** returns `null`. If the given `value` is `text` with a trailing percent symbol, then the converted decimal number will be returned. Otherwise, the value will be converted to a `number` using [Number.From](/powerquery-m/number-from). An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the `percentage` value of `"12.3%"`.

**Usage**

```powerquery-m
Percentage.From("12.3%")
```

**Output**

`0.123`
