---
title: "List.Union | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Union

  
## About  
Returns a list from a list of lists and unions the items in the individual lists. The returned list contains all items in any input lists. Duplicate values are matched as part of the Union.  
  
## Syntax

<pre>
List.Union(list as list,optional equationCriteria as any) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to check.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```powerquery-m
List.Union({ {1..5}, {2..6}, {3..7} }) equals {1..7}  
```  
  
```powerquery-m
List.Union({ {1..5}, {4..8}, {7..11} }) equals {1..11}  
```  
  
```powerquery-m
List.Union({ {1, 1, 1, 2}, {1, 1, 2, 2} }) equals {1, 1, 1, 2, 2}  
```  
