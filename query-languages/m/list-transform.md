---
title: "List.Transform | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Transform

  
## About  
Performs the function on each item in the list and returns the new list.  
  
```  
List.Transform(list as list, transform as function)  as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|transform|The transform to apply.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Transform({1, 2}, each _ + 1) equals { 2, 3 }  
```  
