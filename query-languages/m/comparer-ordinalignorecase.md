---
title: "Comparer.OrdinalIgnoreCase | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Comparer.OrdinalIgnoreCase
<code>Comparer.OrdinalIgnoreCase(**x** as any, **y** as any) as number</code>

## About
Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values <code>x</code> and <code>y</code>.

## Example 
Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using <code>Comparer.Ordinal</code>. 

<code>Comparer.OrdinalIgnoreCase("Abc", "abc")</code>

<code>0</code>