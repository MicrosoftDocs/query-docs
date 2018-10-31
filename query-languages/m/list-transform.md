---
title: "List.Transform | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Transform

  
## About  
Performs the function on each item in the list and returns the new list.  
  
## Syntax

<pre>
List.Transform(list as list, transform as function)  as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|transform|The transform to apply.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
List.Transform({1, 2}, each _ + 1) equals { 2, 3 }  
```  
