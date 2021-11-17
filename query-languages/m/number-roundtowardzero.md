---
description: "Learn more about: Number.RoundTowardZero"
title: "Number.RoundTowardZero | Microsoft Docs"
ms.date: 11/17/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.RoundTowardZero

## Syntax

<pre>
Number.RoundTowardZero(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number
</pre>
  
## About

Returns the result of rounding `number` based on the sign of the number. This function will round positive numbers down and negative numbers up. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits.

## Example 1

Round the number -1.2 toward zero.

``` powerquery-m
Number.RoundTowardZero(-1.2)
```

`-1`

## Example 2

Round the number 1.2 toward zero.

``` powerquery-m
Number.RoundTowardZero(1.2)
```

`1`

## Example 3

Round the number -1.234 to two decimal places toward zero.

``` powerquery-m
Number.RoundTowardZero(-1.234, 2)
```

`-1.23`
