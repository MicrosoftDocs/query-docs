---
title: "List.ReplaceRange | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.ReplaceRange

  
## About  
Returns a list that replaces count values in a list with a replaceWith list starting at an index.  
  
```  
List.ReplaceRange(list as list,  index as number,  count as number,  replaceWith as list) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|index|The index to start at.|  
|count|The number of values to replace.|  
|replaceWith|The value to replace with.|  
  
## Example  
  
```  
List.ReplaceRange({1, 2, 7, 8, 9, 5}, 2, 3, {3, 4}) equals {1, 2, 3, 4, 5}  
```  
