---
title: "List.AnyTrue | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.AnyTrue

  
## About  
Returns true if any expression in a list in true  
  
## Syntax

<pre>
List.AnyTrue(list as list) as logical
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Example  
  
```powerquery-m
List.AnyTrue({2=0, false, 1 < 0 }) equals false  
```  
