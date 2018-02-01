---
title: "List.MaxN | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 9fe27875-1740-46cd-8dc4-ae565f1a99a5
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.MaxN

  
## About  
Returns the maximum values in the list.  After the rows are sorted, optional parameters may be specified to further filter the result  
  
```  
List.MaxN(list as list, countOrCondition as any,  optional comparisonCriteria as any, optional includeNulls as nullable logical) as list  
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
List.MaxN({3, 4, 5, -1, 7, 8, 2}, 5) equals {8, 7, 5, 4, 3}  
```  
