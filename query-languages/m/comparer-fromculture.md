---
description: "Learn more about: Comparer.FromCulture"
title: "Comparer.FromCulture | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Comparer.FromCulture

## Syntax

<pre>
Comparer.FromCulture(<b>culture</b> as text, optional <b>ignoreCase</b> as nullable logical) as function
</pre>
  
## About

Returns a comparer function given the `culture` and a logical value `ignoreCase` for case sensitivity for the comparison. The default value for `ignoreCase` is false. The value for culture are well known text representations of locales used in the .NET framework.

## Example 1

Compare "a" and "A" using "en-US" locale to determine if the values are equal.

**Usage**

```powerquery-m
Comparer.FromCulture("en-US")("a", "A")
```

**Output**

`-1`

## Example 2

Compare "a" and "A" using "en-US" locale ignoring the case to determine if the values are equal.

**Usage**

```powerquery-m
Comparer.FromCulture("en-US", true)("a", "A")
```

**Output**

`0`
