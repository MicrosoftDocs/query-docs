---
title: "List.MaxN | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.MaxN

  
## About  
Returns the maximum values in the list.  After the rows are sorted, optional parameters may be specified to further filter the result  
  
## Syntax

<pre>
List.MaxN(list as list, countOrCondition as any,  optional comparisonCriteria as any, optional includeNulls as nullable logical) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|countOrCondition|Specifies the number of values to return or a filtering condition.|  
|optional comparisonCriteria|Specifies how to compare values in the list.|  
|optional includeNulls|The Logical value whether or not to include null values in the return list.|  
  
## Example  
  
```powerquery-m
List.MaxN({3, 4, 5, -1, 7, 8, 2}, 5) equals {8, 7, 5, 4, 3}  
```  
