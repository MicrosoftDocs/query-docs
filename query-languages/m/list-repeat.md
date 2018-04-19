---
title: "List.Repeat | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Repeat

  
## About  
Returns a list that repeats the contents of an input list count times.  
  
```  
List.Repeat(list as list, count as number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to repeat.|  
|count|The number of times to repeat.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Repeat({1, 2, 3}, 3) equals {1, 2, 3, 1, 2, 3, 1, 2, 3}  
```  
