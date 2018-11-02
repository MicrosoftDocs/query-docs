---
title: "List.ReplaceMatchingItems | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.ReplaceMatchingItems

  
## About  
Replaces occurrences of existing values in the list with new values using the provided equationCriteria. Old and new values are provided by the replacements parameters. An optional equation criteria value can be specified to control equality comparisons. For details of replacement operations and equation criteria, see Parameter Values.  
  
## Syntax

<pre>
List.ReplaceMatchingItems(list as list, replacements as any ,optional equationCriteria as any) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|replacements|The replacements to make.|  
|optional equationCriteria|An optional equation criteria value to control equality testing.|  
  
## Examples  
  
```powerquery-m
List.ReplaceMatchingItems ({1, 2, 3, 4, 5}, {{2, -2}}) equals { 1, -2, 3, 4, 5}  
```  
  
```powerquery-m
List.ReplaceMatchingItems ({1, 2, 3, 4, 5}, {{2, -2}, {3, -3}}) equals { 1, -2, -3, 4, 5}  
```  
