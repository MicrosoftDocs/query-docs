---
title: "List.IsEmpty | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.IsEmpty

  
## About  
Returns whether a list is empty.  
  
## Syntax

<pre>
List.IsEmpty(list as list) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Examples  
  
```powerquery-m
List.IsEmpty({}) equals true  
```  
  
```powerquery-m
List.IsEmpty({1, 2, 3}) equals false  
```  
