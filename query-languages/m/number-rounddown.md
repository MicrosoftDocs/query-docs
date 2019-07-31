---
title: "Number.RoundDown | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.RoundDown

## Syntax

<pre>
Number.RoundDown(<b>number</b> as nullable number, optional <b>digits</b> as nullable number) as nullable number 
</pre>
  
## About  
Returns the result of rounding `number` down to the previous highest integer. If `number` is null, `Number.RoundDown` returns null. If `digits` is specified, `number` is rounded to the `digits` number of decimal digits. 

## Example 1
Round down 1.234 to integer.

```powerquery-m
Number.RoundDown(1.234)
```

`1`

## Example 2
Round down 1.999 to integer.

```powerquery-m
Number.RoundDown(1.999)
```

`1`

## Example 3
Round down 1.999 to two decimal places.

```powerquery-m
Number.RoundDown(1.999, 2)
```

`1.99`
