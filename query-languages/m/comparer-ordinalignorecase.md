---
description: "Learn more about: Comparer.OrdinalIgnoreCase"
title: "Comparer.OrdinalIgnoreCase | Microsoft Docs"
ms.date: 3/8/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Comparer.OrdinalIgnoreCase

## Syntax

<pre>
Comparer.OrdinalIgnoreCase(<b>x</b> as any, <b>y</b> as any) as number
</pre>

## About

Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values `x` and `y`.

## Example 1

Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using `Comparer.Ordinal`.

**Usage**

```powerquery-m
Comparer.OrdinalIgnoreCase("Abc", "abc")
```

**Output**

`0`
