---
title: "Number.RoundUp | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundUp

## Syntax

<pre>
Number.RoundUp(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number
</pre>
  
## About  
Returns the result of rounding `number` down to the previous highest integer. If `number` is null, `Number.RoundDown` returns null. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits. 

## Example 1
Round up 1.234 to integer.

```powerquery-m
Number.RoundUp(1.234)
```

`2`

## Example 2
Round up 1.999 to integer.

```powerquery-m
Number.RoundUp(1.999)
```

`2`

## Example 3
Round up 1.234 to two decimal places.

```powerquery-m
Number.RoundUp(1.234, 2)
```

`1.24`
