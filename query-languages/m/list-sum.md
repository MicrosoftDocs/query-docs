---
title: "List.Sum | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Sum

  
## About  
Returns the sum from a list.  
  
## Syntax

<pre>
List.Sum(list as list) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__toc360789389"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## Examples  
  
```powerquery-m
List.Sum({1, 2, 3}) equals 6  
```  
  
```powerquery-m
List.Sum({#duration(0, 0, 0, 15), #duration(0, 0, 0, 30)}) equals #duration(0, 0, 0, 45)  
```  
  
```powerquery-m
List.Sum({}) equals error  
```  
