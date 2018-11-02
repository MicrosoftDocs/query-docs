---
title: "List.Sort | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Sort

  
## About  
Returns a sorted list using comparison criterion.  
  
## Syntax

<pre>
List.Sort(list as list, optional comparisonCriteria as any ) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|optional comparisonCriteria|Controls the sort order. For more information about equality comparisons, see Parameter Values.|  
  
## <a name="__toc360789351"></a>Remarks  
  
-   To control the order, comparison criterion can be an Order enum value.  
  
-   To compute a key to be used for sorting, a function with one argument can be used.  
  
-   To both select a key and control order, comparison criterion can be a list containing the key and order.  
  
-   To completely control the comparison, a function with two Arguments can be used that returns -1, 0, or 1 given the relationship between the left and right inputs.  Value.Compare is a method that can be used to delegate this logic.  
  
## Examples  
  
```powerquery-m
List.Sort({2, 1}) equals {1, 2}  
```  
  
```powerquery-m
List.Sort({1, 2}, Order.Descending) equals {2, 1}  
```  
  
```powerquery-m
List.Sort({1, 2}, Order.Ascending) equals {1, 2}  
```  
  
```powerquery-m
List.Sort({1, 2}, each 1/_) equals{2, 1}  
```  
  
```powerquery-m
List.Sort({2, 1}, {each 1/_, Order.Descending}) equals {1, 2}  
```  
  
```powerquery-m
List.Sort({1, 2}, (x, y) => Value.Compare(1/x, 1/y)) equals {2, 1}  
```  
