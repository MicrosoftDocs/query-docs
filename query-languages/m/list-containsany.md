---
title: "List.ContainsAny | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.ContainsAny

  
## About  
Returns true if any item in values is found in a list.  
  
```  
List.ContainsAny(list as list, values as list,optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|values|The list of values to check for.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Examples  
  
```  
List.ContainsAny({1, 2, 3}, {2, 4}) equals true  
```  
  
```  
List.ContainsAny({1, 2, 3}, {4, 5}) equals false  
```  
