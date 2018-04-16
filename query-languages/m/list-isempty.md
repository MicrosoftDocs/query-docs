---
title: "List.IsEmpty | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.IsEmpty

  
## About  
Returns whether a list is empty.  
  
```  
List.IsEmpty(list as list) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```  
List.IsEmpty({}) equals true  
```  
  
```  
List.IsEmpty({1, 2, 3}) equals false  
```  
