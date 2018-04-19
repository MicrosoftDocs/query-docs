---
title: "List.Alternate | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Alternate

  
## About  
Returns a list with the items alternated from the original list based on a count, optional repeatInterval, and an optional offset.  
  
```  
List.Alternate(list as list, count as number,  optional repeatInterval as nullable number,  optional offset as nullable number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|count|Alternate count.|  
|optional repeatInterval|Alternate repeat interval.|  
|optional offset|Alternation offset.|  
  
## <a name="__toc360789215"></a>Remarks  
If the repeatInterval and offset are not provided then List.Alternate is equivalent to List.Skip.  
  
## Example  
  
```  
List.Alternate({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, 2, 2, 0) equals {3, 4, 7, 8}  
```  
