---
title: "List.RemoveMatchingItems | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveMatchingItems

  
## About  
Removes all occurrences of the given values in the list.  
  
```  
List.RemoveMatchingItems(list as list, values as list, optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|values|The list of values to remove.|  
|optional equationCriteria|An optional equation criteria value to control equality comparison. For more information about the equationCriteria, see Parameter Values.|  
  
## Example  
  
```  
List.RemoveMatchingItems ({"A", "B", "C", "B", "A"}, {"A", "C"}) equals {"B", "B"}  
```  
