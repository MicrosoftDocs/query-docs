---
title: "List.RemoveNulls | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.RemoveNulls

  
## About  
Removes null values from a list.  
  
## Syntax

<pre>
List.RemoveNulls(list as list) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
  
## Example  
  
```powerquery-m
List.RemoveNulls({1, null, 2}) equals {1, 2}  
```  
