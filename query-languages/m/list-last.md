---
title: "List.Last | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Last

  
## About  
Returns the last set of items in the list by specifying how many items to return or a qualifying condition provided by **countOrCondition**.  
  
## Syntax

<pre>
List.Last(list as list, optional defaultValue as any) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional defaultValue|Default value if list is empty.|  
  
## <a name="__toc360789237"></a>Remarks  
  
-   If a number is specified, up to that many items are returned.  
  
-   If a condition is specified, all items are returned that initially meet the condition. Once an item fails the condition, no further items are considered.  
  
## Examples  
  
```powerquery-m
List.Last({1, 2, 3}) equals 3  
```  
