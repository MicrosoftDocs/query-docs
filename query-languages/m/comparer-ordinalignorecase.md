---
title: "Comparer.OrdinalIgnoreCase | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Comparer.OrdinalIgnoreCase
`Comparer.OrdinalIgnoreCase(**x** as any, **y** as any) as number`

## About
Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values `x` and `y`.

## Example 
Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using `Comparer.Ordinal`. 

`Comparer.OrdinalIgnoreCase("Abc", "abc")`

`0`