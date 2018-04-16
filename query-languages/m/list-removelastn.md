---
title: "List.RemoveLastN | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveLastN

  
## About  
Returns a list with the specified number of elements removed from the list starting at the last element. The number of elements removed depends on the optional countOrCondition parameter.  
  
```  
List.RemoveRange(list as list, offset as number, optional count as nullable number) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to remove items from.|  
|optional countOrCondition|Optional number of elements  or condition to remove elements, default is 1|  
  
## Remarks  
  
-   If countOrCondidtion is omitted only the first element is removed  
  
-   If countOrCondidtion is a number, that many elements (starting from the top) will be removed)  
  
-   If countOrCondidtion is a condition, the elements that meet the condition will be removed until an element does not meet the condition  
  
## Examples  
  
```  
List.RemoveLastN  
  
    (  
  
    {1, 2, 3, 4, 5},  
  
    3  
  
    )  
  
equals {1, 2}  
  
List.RemoveLastN  
  
    (  
  
    {5, 4, 2, 6, 4},  
  
    each _ > 3  
  
    )  
  
equals {5, 4, 2}  
```  
