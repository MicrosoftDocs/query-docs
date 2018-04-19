---
title: "List.Modes | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Modes

  
## About  
Returns all items that appear with the same maximum frequency.  
  
```  
List.Modes(list as list, optional equationCriteria as any)as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Controls the sort order. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789384"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## <a name="__goback"></a>Example  
  
```  
List.Modes({"A", 1, 4, 5, 2, "B", 3, 5, 5, "A", 4, 4, "A"}) equals {"A", 4, 5}  
```  
