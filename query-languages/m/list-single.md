---
title: "List.Single | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Single

  
## About  
Returns the single item of the list or throws an Expression.Error if the list has more than one item.  
  
```  
List.Single(list as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```  
List.Single({1}) equals 1  
```  
  
```  
List.Single({1, 2, 3}) equals error  
```  
