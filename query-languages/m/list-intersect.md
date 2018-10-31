---
title: "List.Intersect | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Intersect

  
## About  
Returns a list from a list of lists and intersects common items in individual lists. Duplicate values are supported.  
  
## Syntax

<pre>
List.Intersect(list as list /* { List } */,optional equationCriteria as any) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to check.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789342"></a>Remarks  
  
-   If nothing is common in all lists, an empty list is returned.  
  
## Examples  
  
```powerquery-m
List.Intersect({ {1..5}, {2..6}, {3..7} }) equals {3..5}  
```  
  
```powerquery-m
List.Intersect({ {1..5}, {4..8}, {7..11} }) equals {}  
```  
  
```powerquery-m 
List.Intersect({ {1, 1, 1, 2}, {1, 1, 2, 2} }) equals {1, 1, 2}  
```  
