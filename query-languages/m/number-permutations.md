---
description: "Learn more about: Number.Permutations"
title: "Number.Permutations | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Number.Permutations

## Syntax

<pre>
Number.Permutations(<b>setSize</b> as nullable number, <b>permutationSize</b> as nullable number) as nullable number
</pre>
  
## About

Returns the number of permutations that can be generated from a number of items, `setSize`, with a specified permutation size, `permutationSize`.

## Example 1

Find the number of permutations from a total of 5 items in groups of 3.

**Usage**

```powerquery-m
Number.Permutations(5, 3)
```

**Output**

`60`
