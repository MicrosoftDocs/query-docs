---
title: "Number.Permutations | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Permutations

  
## About  
Returns the number of total permutatons of a given number of items for the optional permutation size.  
  
## Syntax

<pre>
Number.Permutations(setSize as nullable number, permutationSize as nullable number)  as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|setSize|Number of permutation items.|  
|permutationSize|Size of permutations.|  
  
## Example  
  
```powerquery-m
Number.Permutations(5, 3) equals 60  
```  
