---
title: "List.FirstN | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.FirstN

  
## About  
Returns the first set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.  
  
## Syntax

<pre>
List.FirstN(list as list, countOrCondition as any) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|countOrCondition|The number or condition to qualify against.|  
  
## <a name="__toc360789230"></a>Remarks  
  
-   If a number is specified, up to that many items are returned.  
  
-   If a condition is specified as a function, all items are returned that initially meet the condition.  
  
-   Once an item fails the condition, no further items are considered.  
  
## Examples  
  
```powerquery-m
List.FirstN({3, 4, 5, -1, 7, 8, 2}, 2) equals {3, 4}  
```  
  
```powerquery-m
List.FirstN({3, 4, 5, -1 ,7, 8, 2}, each_ > 2) equals {3, 4, 5}  
```  
