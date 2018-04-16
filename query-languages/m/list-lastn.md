---
title: "List.LastN | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.LastN

  
## About  
Returns the last set of items in a list by specifying how many items to return or a qualifying condition.  
  
```  
List.LastN(list as list, optional countOrCondition as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional countOrCondition|Number items to return or a qualifying condition.|  
  
## <a name="__toc360789241"></a>Remarks  
  
-   If a number is specified, up to that many items are returned.  
  
-   If a condition is specified, all items are returned that initially meet the condition.  
  
-   Once an item fails the condition, no further items are considered  
  
## Example  
  
```  
List.LastN({3, 4, 5, -1, 7, 8, 2},1) equals  { 2 }  
```  
