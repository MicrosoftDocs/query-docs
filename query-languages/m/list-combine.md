---
title: "List.Combine | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Combine

  
## About  
Merges a list of lists into single list.  
  
```  
List.Combine(list as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List of lists to merge.|  
  
## Example  
  
```  
List.Combine({ {1, 2, 3, 4}, {5, 6, 7}, {8, 9} }) equals {1, 2, 3, 4, 5, 6, 7, 8, 9}  
```  
