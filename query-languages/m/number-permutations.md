---
title: "Number.Permutations | Microsoft Docs"
ms.date: 7/31/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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

```powerquery-m
Number.Permutations(5, 3)
```

`60`
