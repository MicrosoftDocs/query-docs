---
title: "List.Select | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Select

  
## About  
Selects the items that match a condition.  
  
```  
List.Select(list as list, condition as function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|condition|The condition to match against.|  
  
## <a name="__goback"></a>Example  
  
```  
List.Select({1, 3, 5}, each _ > 2) equals {3 ,5}  
```  
