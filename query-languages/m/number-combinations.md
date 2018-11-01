---
title: "Number.Combinations | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Combinations

  
## About  
Returns the number of combinations of a given number of items for the optional combination size.  
  
## Syntax

<pre>
Number.Combinations (setSize as nullable number,  combinationSize as nullable number)  as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|setSize|Number of combination items.|  
|combinationSize|Size of combinations.|  
  
## Example  
  
```powerquery-m
Number.Combinations(5, 3) equals 10  
```  
