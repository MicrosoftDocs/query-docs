---
title: "List.RemoveItems | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveItems

  
## About  
Removes items from list1 that are present in list2, and returns a new list.  
  
```  
List.RemoveItems(list1 as list, list2 as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list1|The List to modify.|  
|list2|The list of items to remove.|  
  
## Example  
  
```  
List.RemoveItems({1, 2, 3, 3}, {3}) equals { 1, 2}  
```  
