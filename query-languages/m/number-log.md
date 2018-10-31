---
title: "Number.Log | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Log
`Number.Log(**number** as nullable number, optional **base** as nullable number) as nullable number`

## About
Returns the logarithm of a number, `number`, to the specified `base` base. If `base` is not specified, the default value is Number.E. If `number` is null `Number.Log` returns null.

## Example 1
Get the base 10 logarithm of 2.


```
Number.Log(2, 10)
```


```
0.3010299956639812
```

## Example 2
Get the base e logarithm of 2.


```
Number.Log(2)
```

```
0.69314718055994529
```


