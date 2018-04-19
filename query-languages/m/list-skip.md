---
title: "List.Skip | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Skip

  
## About  
Skips the first item of the list.  Given an empty list, it returns an empty list. This function takes an optional parameter countOrCondition to support skipping multiple values.  
  
```  
List.Skip(list as list, optional countOrCondition as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional countOrCondition|An optional parameter that skips multiple values.|  
  
## <a name="__toc360789265"></a>Remarks  
  
-   If a number is specified, up to that many items are skipped.  
  
-   If a condition is specified, all items that meet the condition are skipped.  Once an item fails the condition, no further items are considered.  
  
-   If this parameter is null, the default behavior is observed.  
  
## Examples  
  
```  
List.Skip({3, 4, 5, -1, 7, 8, 2}) equals {4, 5, -1, 7, 8, 2}  
```  
  
```  
List.Skip({}) equals {}  
```  
  
```  
List.Skip({3, 4, 5, -1, 7, 8, 2}, 5) equals {8, 2}  
```  
  
```  
List.Skip({3, 4, 5}, 5) equals {}  
```  
  
```  
List.Skip({3, 4, 5, -1, 7, 8, 2}, each _ > 0) equals {-1, 7, 8, 2}  
```  
  
```  
List.Skip({3, 4, 5}, each _ > 0) equals {}  
```  
  
```  
List.Skip({3, 4, 5, -1, 7, 8, 2}, null) equals {4, 5, -1, 7, 8, 2}  
```  
