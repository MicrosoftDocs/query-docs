---
description: "Learn more about: Number.RoundUp"
title: "Number.RoundUp | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number.RoundUp

## Syntax

<pre>
Number.RoundUp(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number
</pre>
  
## About

Returns the result of rounding `number` down to the previous highest integer. If `number` is null, **Number.RoundDown** returns null. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits.

## Example 1

Round up 1.234 to integer.

**Usage**

```powerquery-m
Number.RoundUp(1.234)
```

**Output**

`2`

## Example 2

Round up 1.999 to integer.

**Usage**

```powerquery-m
Number.RoundUp(1.999)
```

**Output**

`2`

## Example 3

Round up 1.234 to two decimal places.

**Usage**

```powerquery-m
Number.RoundUp(1.234, 2)
```

**Output**

`1.24`
