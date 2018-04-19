---
title: "List.Range | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Range

  
## About  
Returns a count items starting at an offset.  
  
```  
List.Range(list as list, offset as number, optional count as number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|offset|The index to start at.|  
|optional count|Count of items to return.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Range({1..10}, 3, 5)  equals  {4, 5, 6, 7, 8}  
```  
