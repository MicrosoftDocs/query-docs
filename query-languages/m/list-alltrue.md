---
title: "List.AllTrue | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.AllTrue

  
## About  
Returns true if all expressions in a list are true  
  
```  
List.AllTrue(list as list) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Example  
  
```  
List.AllTrue({true, 2=2}) equals true  
```  
