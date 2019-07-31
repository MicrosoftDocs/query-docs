---
title: "Number.Log | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Log

## Syntax

<pre>
Number.Log(<b>number</b> as nullable number, optional <b>base</b> as nullable number) as nullable number
</pre>

## About
Returns the logarithm of a number, `number`, to the specified `base` base. If `base` is not specified, the default value is Number.E. If `number` is null `Number.Log` returns null.

## Example 1
Get the base 10 logarithm of 2.

```powerquery-m
Number.Log(2, 10)
```

`0.3010299956639812`

## Example 2
Get the base e logarithm of 2.


```powerquery-m
Number.Log(2)
```

`0.69314718055994529`


