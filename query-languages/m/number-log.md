---
title: "Number.Log | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Log
<code>Number.Log(**number** as nullable number, optional **base** as nullable number) as nullable number</code>

## About
Returns the logarithm of a number, <code>number</code>, to the specified <code>base</code> base. If <code>base</code> is not specified, the default value is Number.E. If <code>number</code> is null <code>Number.Log</code> returns null.

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


