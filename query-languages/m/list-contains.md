---
title: "List.Contains | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Contains

  
## About  
Returns true if a value is found in a list.  
  
## Syntax

<pre>
List.Contains(list as list, value as any, optional equationCriteria as any) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|value|The value to check for.|  
|optional equationCriteria|An optional equation criteria value to control equality testing.|  
  
## Examples  
  
```powerquery-m
List.Contains({1, 2, 3}, 2) equals true  
```  
  
```powerquery-m
List.Contains({1, 2, 3}, 4) equals false  
```  
