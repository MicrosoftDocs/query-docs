---
title: "List.RemoveRange | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveRange

  
## About  
Returns a list that removes count items starting at offset.  The default count is 1.  
  
## Syntax

<pre>
List.RemoveRange(list as list, offset as number, optional count as nullable number) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to remove items from.|  
|offset|The index to start at.|  
|optional count|The number of items to remove.|  
  
## Examples  
  
```powerquery-m
List.RemoveRange({"A", "B", "C", "D"}, 2) equals {"A", "B", "D"}  
```  
  
```powerquery-m
List.RemoveRange({"A", "B", "C", "D"}, 1, 2) equals {"A", "D"}  
```  
