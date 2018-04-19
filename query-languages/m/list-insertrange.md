---
title: "List.InsertRange | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.InsertRange

  
## About  
Inserts items from values at the given index in the input list.  
  
```  
List.InsertRange(list as list, offset as number, values as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|offset|The index to insert at.|  
|values|The values to insert.|  
  
## <a name="__goback"></a>Example  
  
```  
List.InsertRange({"A", "B", "D"}, 2, {"C"}) equals {"A", "B", "C", "D"}  
```  
