---
title: "Function.From | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Function.From

## Syntax

<pre>
Function.From(<b>functionType</b> as type, <b>function</b> as function) as function
</pre>

## About
Takes a unary function `function` and creates a new function with the type `functionType` that constructs a list out of its arguments and passes it to `function`.

## Example 1
Converts List.Sum into a two-argument function whose arguments are added together.

```powerquery-m
Function.From(type function (a as number, b as number) as number, List.Sum)(2, 1)
```

`3`

## Example 2
Converts a function taking a list into a two-argument function.

```powerquery-m
Function.From(type function (a as text, b as text) as text, (list) => list{0} & list{1})("2", "1")
```

`"21"`

