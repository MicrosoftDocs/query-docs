---
title: "Comparer.OrdinalIgnoreCase | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Comparer.OrdinalIgnoreCase

## Syntax

<pre>
Comparer.OrdinalIgnoreCase(<b>x</b> as any, <b>y</b> as any) as number
</pre>

## About
Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values `x` and `y`.

## Example 
Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using `Comparer.Ordinal`. 

```powerquery-m
Comparer.OrdinalIgnoreCase("Abc", "abc")
```

```powerquery-m
0
```