---
title: "List.MinN | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.MinN

  
## About  
Returns the minimum values in a list.  
  
```  
List.MinN(list as list, countOrCondition as any,  optional comparisonCriteria as any, optional includeNulls as nullable logical) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|countOrCondition|Specifies the number of values to return or a filtering condition.|  
|optional comparisonCriteria|Specifies how to compare values in the list.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```  
List.MinN({3, 4, 5, -1, 7, 8, 2}, 5) equals {-1, 2, 3, 4, 5}  
```  
