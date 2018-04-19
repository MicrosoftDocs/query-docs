---
title: "List.Count | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Count

  
## About  
Returns the number of items in a list.  
  
```  
List.Count(list as list) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```  
List.Count({1,2,3}) equals 3  
```  
  
```  
List.Count({}) equals 0  
```  
