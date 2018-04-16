---
title: "List.AnyTrue | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.AnyTrue

  
## About  
Returns true if any expression in a list in true  
  
`List.AnyTrue(list as list) as logical`  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Example  
  
```  
List.AnyTrue({2=0, false, 1 < 0 }) equals false  
```  
