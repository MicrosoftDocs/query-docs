---
title: "List.AllTrue | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.AllTrue

  
## About  
Returns true if all expressions in a list are true  
  
## Syntax

<pre>
List.AllTrue(list as list) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Example  
  
```powerquery-m
List.AllTrue({true, 2=2}) equals true  
```  
