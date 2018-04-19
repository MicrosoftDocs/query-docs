---
title: "List.RemoveNulls | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveNulls

  
## About  
Removes null values from a list.  
  
```  
List.RemoveNulls(list as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
  
## Example  
  
```  
List.RemoveNulls({1, null, 2}) equals {1, 2}  
```  
