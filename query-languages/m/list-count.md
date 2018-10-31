---
title: "List.Count | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Count

  
## About  
Returns the number of items in a list.  
  
## Syntax

<pre>
List.Count(list as list) as number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```powerquery-m
List.Count({1,2,3}) equals 3  
```  
  
```powerquery-m
List.Count({}) equals 0  
```  
