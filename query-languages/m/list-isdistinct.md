---
title: "List.IsDistinct | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.IsDistinct

  
## About  
Returns whether a list is distinct.  
  
## Syntax

<pre>
List.IsDistinct(list as list, optional equationCriteria as any) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional equationCriteria|Equation criteria value used to control equality comparison. For more information about equationCriteria, see Parameter Values.|  
  
## Examples  
  
```powerquery-m
List.IsDistinct({1, 2, 3, 2, 3}) equals false  
```  
  
```powerquery-m
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",false) equals true  
```  
  
```powerquery-m
List.IsDistinct({"a","b","A"}, Comparer.FromCulture("en",true) equals false  
```  
