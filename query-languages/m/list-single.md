---
title: "List.Single | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Single

  
## About  
Returns the single item of the list or throws an Expression.Error if the list has more than one item.  
  
## Syntax

<pre>
List.Single(list as list) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```powerquery-m
List.Single({1}) equals 1  
```  
  
```powerquery-m
List.Single({1, 2, 3}) equals error  
```  
