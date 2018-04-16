---
title: "List.IsDistinct | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.IsDistinct

  
## About  
Returns whether a list is distinct.  
  
```  
List.IsDistinct(list as list, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Equation criteria value used to control equality comparison. For more information about equationCriteria, see Parameter Values.|  
  
## Examples  
  
```  
List.IsDistinct({1, 2, 3, 2, 3}) equals false  
```  
  
```  
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",false) equals true  
```  
  
```  
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",true) equals false  
```  
