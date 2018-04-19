---
title: "List.ContainsAll | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.ContainsAll

  
## About  
Returns true if all items in values are found in a list.  
  
```  
List.ContainsAll(list as list, values as list,optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|values|The list of values to check for.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.ContainsAll({1, 2, 3}, {2, 3}) equals true  
```  
  
```  
List.ContainsAll({1, 2, 3}, {2, 4}) equals false  
```  
